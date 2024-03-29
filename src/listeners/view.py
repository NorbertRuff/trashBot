"""
Handles the view submission events
"""

from logging import Logger

from slack_bolt import App, Ack, Respond, Say
from slack_sdk import WebClient

from src import utils, data_manager
from src.blocks import get_rating_section
from src.data_manager import ChallengeCategory
from src.slack_bot import TrashBot


# <------------------------views------------------------------->
class ViewSubmissionListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.view("send_user_trash_modal")(self.handle_modal_submission_trash_to_user)
        self.app.view("send_channel_trash_modal")(self.handle_modal_submission_trash_to_channel)
        self.app.view("send_channel_challenge_modal")(self.handle_modal_submission_challenge_to_channel)
        self.app.view("save_challenge_modal")(self.handle_modal_submission_save_challenge_to_db)
        self.app.view("save_trash_modal")(self.handle_modal_submission_trash_save)

    def handle_modal_submission_trash_to_user(self, payload: dict, body: dict, client: WebClient, ack: Ack,
                                              respond: Respond, logger: Logger):
        """Gets called when a user submits the modal to send trash to a user"""
        logger.info(body)
        logger.info(payload)
        sender = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        video_id = payload.get("blocks")[1].get("alt_text") if payload.get("blocks") else None
        video_db_row = utils.get_random_video_db_row() if not video_id else data_manager.get_video_by_video_id(video_id)
        message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
        recipient = values.get("selected_user", "").get("selected_user", "").get("selected_user", "")
        dm_channel = client.conversations_open(users=recipient)
        channel = dm_channel.get("channel", {}).get("id", "")
        errors = {}
        if not channel:
            errors["selected_user"] = "Could not open DM with user"
            ack(response_action="errors", errors=errors)
        text = self.bot.generate_dm_text(sender_user_id=sender, recipient_user_id=recipient, message=message_to_send,
                                         video_db_row=video_db_row)
        client.chat_postMessage(channel=channel, text=text)
        ack()

    def handle_modal_submission_trash_to_channel(self, payload: dict, body: dict, client: WebClient, ack: Ack, say: Say,
                                                 logger: Logger):
        """Gets called when a user submits the modal to send trash to a channel"""
        logger.info(body)
        sender_user_id = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
        video_db_row = utils.get_random_video_db_row()
        video_id = video_db_row.get("video_id", "")
        text = self.bot.generate_bot_post_to_channel(sender_user_id=sender_user_id, message=message_to_send,
                                                     video_db_row=video_db_row)
        client.chat_postMessage(channel=self.trash_channel_id, text=text)
        say(channel=self.trash_channel_id, text=get_rating_section(video_id=video_id))
        ack()

    def handle_modal_submission_challenge_to_channel(self, payload: dict, body: dict, client: WebClient, ack: Ack,
                                                     say: Say,
                                                     logger: Logger):
        """Gets called when a user submits the modal to send challenge to a channel"""
        logger.info(body)
        sender_user_id = body.get("user", "").get("id", "")
        challenge = data_manager.get_random_challenge()
        if not challenge:
            ack()
            logger.debug("No active challenges left in database")
            return
        challenge_id = challenge.get("id", "")
        data_manager.update_challenge_status(challenge_id=challenge_id, status="completed")
        text = self.bot.generate_bot_challenge_post_to_channel(challenge=challenge)
        client.chat_postMessage(channel=self.trash_channel_id, text=text)
        ack()

    def handle_modal_submission_save_challenge_to_db(self, payload: dict, body: dict, client: WebClient, ack: Ack,
                                                     say: Say,
                                                     logger: Logger):
        """Gets called when a user submits the modal to save challenge to database"""
        logger.info(body)
        user_id = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        logger.info(values)
        challenge_type = values.get("challenge_type", "") \
            .get("static_select_type", "") \
            .get("selected_option", "") \
            .get("value", "")
        challenge_category = values.get("challenge_category", "") \
            .get("static_select_category", "") \
            .get("selected_option", "") \
            .get("value", "")
        challenge_text = values.get("challenge_text", "") \
            .get("challenge_text", "") \
            .get("value", "")
        logger.debug(ChallengeCategory[challenge_category].value)
        data_manager.add_challenge(challenge_type=challenge_type,
                                   challenge_category=ChallengeCategory[challenge_category].value,
                                   challenge_text=challenge_text, user_id=user_id)
        ack()

    def handle_modal_submission_trash_save(self, payload: dict, client: WebClient, body: dict, ack: Ack,
                                           logger: Logger):
        """Gets called when a user submits the modal to save trash to the database"""
        logger.info(body)
        sender_user_id = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        youtube_url = values.get("youtube_url", "").get("youtube_url", "").get("value", "")
        video_id = utils.match_youtube_url(youtube_url)
        errors = {}
        if not video_id:
            errors["youtube_url"] = "Invalid youtube url"
            ack(response_action="errors", errors=errors)
        youtube_data = utils.get_youtube_video_info(video_id)
        if not youtube_data:
            errors["youtube_url"] = "Invalid youtube url"
            ack(response_action="errors", errors=errors)
        if data_manager.video_exists(video_id)['exists']:
            errors["youtube_url"] = "Video already exists"
            ack(response_action="errors", errors=errors)
        data_manager.put_video_in_table(video_id=video_id, user_id=sender_user_id, fallback=youtube_data['title'],
                                        title=youtube_data['title'],
                                        author_name=youtube_data['author_name'])
        client.chat_postMessage(channel=self.trash_channel_id, text=self.bot.new_video_added())
        ack()

from logging import Logger

from slack_bolt import App, Ack, Respond
from slack_sdk import WebClient

from src import utils
from src.slack_bot import TrashBot


# <------------------------views------------------------------->
class ViewListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.view("send_user_trash_modal")(self.handle_modal_submission_trash_to_user)
        self.app.view("send_channel_trash_modal")(self.handle_modal_submission_trash_to_channel)

    def handle_modal_submission_trash_to_user(self, payload: dict, body: dict, client: WebClient, ack: Ack,
                                              respond: Respond, logger: Logger):
        logger.info(body)
        ack()
        sender = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
        recipient = values.get("selected_user", "").get("selected_user", "").get("selected_user", "")
        video_db_row = utils.get_random_video_db_row()
        dm_channel = client.conversations_open(users=recipient)
        channel = dm_channel.get("channel", {}).get("id", "")
        if not channel:
            respond("Could not open DM with user")
        text = self.bot.generate_dm_text(sender_user_id=sender, recipient_user_id=recipient, message=message_to_send,
                                         video_db_row=video_db_row)
        client.chat_postMessage(channel=channel, text=text)

    def handle_modal_submission_trash_to_channel(self, payload: dict, body: dict, client, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        sender_user_id = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
        video_db_row = utils.get_random_video_db_row()
        text = self.bot.generate_bot_post_to_channel(sender_user_id=sender_user_id, message=message_to_send,
                                                     video_db_row=video_db_row)
        client.chat_postMessage(channel=self.trash_channel_id, text=text)

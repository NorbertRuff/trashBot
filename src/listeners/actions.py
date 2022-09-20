import re
from logging import Logger

from slack_bolt import App, Ack, Say
from slack_sdk import WebClient

from src import data_manager
from src.slack_bot import TrashBot
from src.utils import blocks


# # <------------------------action------------------------------->
class ActionListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.action(re.compile("rate_video"))(self.rating_button_click)
        self.app.action("send_to_user_from_list_button_action")(self.handle_open_send_trash_to_user_modal)
        self.app.action(re.compile("send_to_channel_button_action"))(self.handle_send_to_channel_button_action)
        self.app.action("open_send_trash_to_channel_modal")(self.handle_open_send_trash_to_channel_modal)
        self.app.action("open_send_trash_to_user_modal")(self.handle_open_send_random_trash_to_user_modal)
        self.app.action("open_list_trash_videos_modal")(self.handle_open_list_trash_videos_modal)
        self.app.action(re.compile("navigate"))(self.handle_navigate)
        self.app.action("home_button")(self.handle_back_to_home)

    def rating_button_click(self, body: dict, ack: Ack, logger: Logger):
        # Acknowledge the action
        logger.info(body)
        ack()
        user_id = body.get("user", "").get("id", "")
        value = body['actions'][0]['value'] if 'actions' in body else None
        video_id = value.split(" ")[0]
        rating = value.split(" ")[1]
        logger.info(f"User {user_id} rated video {video_id} with {rating}")
        if data_manager.user_already_rated(video_id, user_id)['exists']:
            logger.info(f"User {user_id} already rated video {video_id}")
            return
        data_manager.insert_rating(video_id, user_id, rating)

    def handle_send_to_channel_button_action(self, client: WebClient, body: dict, ack: Ack, say: Say, logger: Logger):
        logger.info(body)
        ack()
        user_id = body.get("user", "").get("id", "")
        value = body['actions'][0]['value'] if 'actions' in body else None
        video_id = value.split(" ")[1]
        video_db_row = data_manager.get_video_by_id(video_id)
        text = self.bot.generate_bot_post_to_channel(sender_user_id=user_id, message="", video_db_row=video_db_row)
        client.chat_postMessage(text=text, channel=self.trash_channel_id)
        say(channel=self.trash_channel_id, text=blocks.get_rating_section(video_db_row.get("video_id", "")))

    def handle_open_send_random_trash_to_user_modal(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=blocks.get_send_trash_to_user_modal()
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_open_send_trash_to_user_modal(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        video_id = body['actions'][0]['value']
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=blocks.get_send_trash_to_user_modal(video_id=video_id)
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_open_send_trash_to_channel_modal(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=blocks.get_send_trash_to_channel_modal()
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_open_list_trash_videos_modal(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        videos = data_manager.get_all_videos()
        user_id = body.get("user").get("id", "")
        try:
            client.views_publish(
                user_id=user_id,
                view=blocks.get_video_list_modal(videos=videos, offset=0)
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_navigate(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        page = int(body['actions'][0]['value'])
        videos = data_manager.get_all_videos()
        try:
            client.views_update(
                view_id=body['container']['view_id'],
                view=blocks.get_video_list_modal(videos, page)
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_back_to_home(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        user_id = body.get("user").get("id", "")
        try:
            client.views_publish(
                user_id=user_id,
                view=blocks.get_home_view_blocks(user_id)
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

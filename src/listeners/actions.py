import re
from logging import Logger

from slack_bolt import App, Ack
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
        self.app.action(re.compile("send_to_channel_button_action"))(self.handle_send_to_channel_button_action)
        self.app.action("open_send_trash_to_channel_modal")(self.handle_open_send_trash_to_channel_modal)
        self.app.action("open_send_trash_to_user_modal")(self.handle_open_send_trash_to_user_modal)
        self.app.action("open_list_trash_videos_modal")(self.handle_open_list_trash_videos_modal)

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

    def handle_send_to_channel_button_action(self, client: WebClient, body: dict, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        user_id = body.get("user", "").get("id", "")
        value = body['actions'][0]['value'] if 'actions' in body else None
        video_id = value.split(" ")[1]
        print(video_id)
        video_db_row = data_manager.get_video_by_id(video_id)
        print(video_db_row)
        text = self.bot.generate_bot_post_to_channel(sender_user_id=user_id, message="", video_db_row=video_db_row)
        client.chat_postMessage(text=text, channel=self.trash_channel_id)

    def handle_open_send_trash_to_user_modal(self, body: dict, client: WebClient, ack: Ack, logger: Logger):
        logger.info(body)
        ack()
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=blocks.get_send_trash_to_user_modal()
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
                view=blocks.get_video_list_modal(videos, 0)
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

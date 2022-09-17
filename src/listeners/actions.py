import logging
import re

from slack_bolt import App, Ack

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
        self.app.action("open_send_trash_to_channel_modal")(self.handle_open_send_trash_to_channel_modal)
        self.app.action("open_send_trash_to_user_modal")(self.handle_open_send_trash_to_user_modal)

    def rating_button_click(self, body: dict, ack: Ack, logger: logging.Logger):
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

    def handle_open_send_trash_to_user_modal(self, body: dict, client: App.client, ack: Ack, logger: logging.Logger):
        logger.info(body)
        ack()
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=blocks.get_send_trash_to_user_modal()
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_open_send_trash_to_channel_modal(self, body: dict, client: App.client, ack: Ack, logger: logging.Logger):
        logger.info(body)
        ack()
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=blocks.get_send_trash_to_channel_modal()
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

import logging

from slack_bolt import App, Respond, Ack

from src.slack_bot import TrashBot
from src.utils import save_video


# <------------------------shortcut------------------------------->
class ShortcutListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.shortcut("save_shortcut")(self.handle_save_shortcut)

    def handle_save_shortcut(self, body: dict, respond: Respond, ack: Ack, logger: logging.Logger):
        """Save a video to the playlist"""
        logger.info(body)
        ack()
        text = body.get("message", "").get("text", "")
        user_id = body.get("user", "").get("id", "")
        response = save_video(text, user_id, self.bot)
        respond(response)

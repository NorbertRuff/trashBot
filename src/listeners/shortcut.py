from logging import Logger

from slack_bolt import App, Respond, Ack
from slack_sdk import WebClient

from src.slack_bot import TrashBot, TRASH_BOT_VIDEO_ADDED
from src.utils import save_video


# <------------------------shortcut------------------------------->
class ShortcutListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.shortcut("save_shortcut")(self.handle_save_shortcut)

    def handle_save_shortcut(self, body: dict, client: WebClient, respond: Respond, ack: Ack, logger: Logger):
        """Save a video to the playlist"""
        logger.info(body)
        ack()
        text = body.get("message", "").get("text", "")
        user_id = body.get("user", "").get("id", "")
        response = save_video(text, user_id, self.bot)
        if TRASH_BOT_VIDEO_ADDED in response:
            client.chat_postMessage(channel=self.trash_channel_id, text=self.bot.new_video_added())
        respond(response)

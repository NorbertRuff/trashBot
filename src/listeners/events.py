"""
This Listener is responsible for handling events in the slack workspace.
"""

from logging import Logger

from slack_bolt import Ack, Say, App
from slack_sdk import WebClient

from src import utils
from src.blocks import get_home_view_blocks
from src.slack_bot import TrashBot, TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS, TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS
from src.utils import save_video


# # <------------------------events------------------------------->
class EventListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.event("message")(self.handle_message_events)
        self.app.event("app_mention")(self.handle_bot_mention)
        self.app.event("emoji_changed")(self.handle_emoji_changed_events)
        self.app.event("app_home_opened")(self.handle_app_home_open_event)

    def handle_message_events(self, event: dict, say: Say, ack: Ack, logger: Logger):
        """Handle message events"""
        ack()
        subtype = event.get("subtype", "")
        channel = event.get("channel", "")
        user = event.get("user", "")
        if channel != self.trash_channel_id:
            return
        if utils.user_is_bot(user, self.bot.bot_id):
            return
        if not user:
            return
        if subtype == "channel_join" and channel == self.trash_channel_id:
            logger.info(event)
            text = self.bot.ask_for_introduction(user)
            say(channel=self.trash_channel_id, text=text)

    def handle_bot_mention(self, body: dict, event: dict, say: Say, ack: Ack, logger: Logger):
        """Handle slackBot mention"""
        logger.info(body)
        ack()
        text = event.get("text", "")
        user = event.get("user", "")
        message = self.handle_event_text(text, user, say)
        if message:
            say(message)

    def handle_emoji_changed_events(self, event: dict, say: Say, ack: Ack, logger: Logger):
        """Handle emoji changed events"""
        logger.info(event)
        ack()
        emoji_name = event.get("name", "")
        subtype = event.get("subtype", "")
        if subtype == "add":
            say(
                channel=self.trash_channel_id,
                text=self.bot.get_emoji_event_response(emoji_name)
            )

    def handle_app_home_open_event(self, event: dict, client: WebClient, ack: Ack, logger: Logger):
        """Handle app home open event"""
        logger.info(event)
        ack()
        user_id = event.get("user")
        try:
            client.views_publish(
                user_id=user_id,
                view=get_home_view_blocks(user_id)
            )
        except Exception as e:
            logger.error(f"Error publishing view to Home Tab: {e}")

    def handle_event_text(self, text: str, user: str, say: Say) -> str:
        """Handle a slackBot commands"""
        if "help" in text.lower():
            return self.bot.help()
        if any(word in text.lower() for word in TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS):
            return utils.get_random_video_response(say, self.bot)
        if any(word in text.lower() for word in TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS):
            return save_video(text, user, self.bot)
        if "good bot" in text.lower():
            return self.bot.random_love_reply()
        if "bad bot" in text.lower():
            return self.bot.random_hate_reply()
        if "source code" in text.lower():
            return 'https://github.com/NorbertRuff/trashBot'
        return self.bot.random_dont_understand()

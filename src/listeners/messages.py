"""
Handles the messages sent to the bot
"""

import re
from logging import Logger

from slack_bolt import App, Ack, Say

from src import utils
from src.slack_bot import TrashBot


# <------------------------message------------------------------->
class MessageListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.message(re.compile("hello"))(self.handle_hello)
        self.app.message(re.compile("good bot"))(self.handle_bot_love)
        self.app.message(re.compile("bad bot"))(self.handle_bot_hate)

    def handle_hello(self, message: dict, say: Say, ack: Ack, logger: Logger):
        """Handle hello message"""
        logger.info(message)
        ack()
        user = message.get("user", "")
        if utils.user_is_bot(user, self.bot.bot_id):
            return
        say(self.bot.say_hi_to(user))
        # blocks = []
        # blocks.append(utils.blocks.get_video_block_from_yt_details(video_details))
        # say(channel=self.trash_channel_id, text="asdfd", blocks=blocks)

    def handle_bot_love(self, message: dict, say: Say, ack: Ack, logger: Logger):
        """Handle hello message"""
        logger.info(message)
        ack()
        user = message.get("user", "")
        if utils.user_is_bot(user, self.bot.bot_id):
            return
        say(self.bot.random_love_reply())

    def handle_bot_hate(self, message: dict, say: Say, ack: Ack, logger: Logger):
        """Handle hello message"""
        logger.info(message)
        ack()
        user = message.get("user", "")
        if utils.user_is_bot(user, self.bot.bot_id):
            return
        say(self.bot.random_hate_reply())

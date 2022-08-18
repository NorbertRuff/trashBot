import random

from src.bot import *
from src.bot.bot_messages import *


class TrashBot:
    def __init__(self, bot_id, name):
        self.bot_id: bot_id
        self.name: name

    def say_hi_to(self, user: object) -> str:
        """Say hi to user :return: str"""
        return f"Hello! <@{user}> :wave:"

    def random_general_reply(self) -> str:
        """TrashBot random general message :return: str"""
        return random.choice(TRASH_BOT_GENERAL_REPLIES)

    def random_success_reply(self) -> str:
        """TrashBot random success message :return: str"""
        return random.choice(TRASH_BOT_SUCCESS_REPLIES)

    def random_error_reply(self) -> str:
        """TrashBot random error message :return: str"""
        return random.choice(TRASH_BOT_ERROR_REPLIES)

    def random_hate_reply(self) -> str:
        """TrashBot random hate message :return: str"""
        return random.choice(TRASH_BOT_HATE)

    def random_love_reply(self) -> str:
        """TrashBot random love reply :return: str"""
        return random.choice(TRASH_BOT_LOVE)

    def get_reply_text(self, receiver: str, user_id: str) -> str:
        """TrashBot random love reply :return: str"""
        return f"Hey {receiver}! <@{user_id}> just sent random video for you!\n"

    def get_reply_text_with_message(self, receiver: str, user_id: str, message: str) -> str:
        """TrashBot random love reply :return: str"""
        return f"Hey {receiver}! <@{user_id}> just sent random video for you! \n\nMessage: \"{message}\".\n\n"

    def help(self) -> str:
        """TrashBot help message :return: str"""
        return TRASHBOT_HELP_MSG

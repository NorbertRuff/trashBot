import random
from bot_messages import *


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

    def help(self) -> str:
        """TrashBot help message :return: str"""
        return TRASHBOT_HELP_MSG

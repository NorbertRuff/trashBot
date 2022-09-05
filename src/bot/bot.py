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

    def general_error_reply(self) -> str:
        """TrashBot random error message :return: str"""
        return TRASH_BOT_SHIT_HIT_THE_FAN

    def random_hate_reply(self) -> str:
        """TrashBot random hate message :return: str"""
        return random.choice(TRASH_BOT_HATE)

    def random_love_reply(self) -> str:
        """TrashBot random love reply :return: str"""
        return random.choice(TRASH_BOT_LOVE)

    def get_reply_text(self, receiver: str, user_id: str) -> str:
        """TrashBot reply without message for messaging functionality
        :param user_id: the user who sent the message
        :param receiver: the user who will receive the message
        :return: str
        """
        return f"Hey {receiver}! <@{user_id}> just sent random video for you!\n"

    def get_reply_text_with_message(self, receiver: str, user_id: str, message: str) -> str:
        """TrashBot reply with message for messaging functionality
        :param user_id: the user who sent the message
        :param message: the message that the user sent
        :param receiver: the user who will receive the message
        :return: str
        """
        return f"Hey {receiver}! <@{user_id}> just sent random video for you! \n\nMessage: \"{message}\".\n\n"

    def get_reply_text_from_video_row(self, video: list or None) -> str:
        """TrashBot reply with message for messaging functionality"""
        return f"video #{video['id']} https://www.youtube.com/watch?v={video['video_id']} video rating: {video['rating']} /5 "

    def ask_for_introduction(self, user_name) -> str:
        return f"Welcome to the random channel, <@{user_name}>! 🎉 You should introduce yourself to the rest of the team with an energizing trash video. 🎉"

    def get_emoji_event_response(self, emoji_name) -> str:
        return random.choice(TRASH_BOT_EMOJI_REPLIES) + f" -> :{emoji_name}:"

    def help(self) -> str:
        """TrashBot help message :return: str"""
        return TRASHBOT_HELP_MSG

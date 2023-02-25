"""
A Bot class that handles all the Slack bot replies
"""
import random

from .bot_messages import TRASHBOT_HELP_MSG, TRASH_BOT_EMOJI_REPLIES, TRASH_BOT_LOVE, TRASH_BOT_HATE, \
    TRASH_BOT_SHIT_HIT_THE_FAN, TRASH_BOT_ERROR_REPLIES, TRASH_BOT_SUCCESS_REPLIES, TRASH_BOT_GENERAL_REPLIES, \
    TRASH_BOT_NOT_FOUND_LINK, TRASH_BOT_DONT_UNDERSTAND, TRASH_BOT_NEW_VIDEO_ADDED, TRASH_BOT_CHALLENGE_TITLE


class TrashBot:
    def __init__(self, bot_id, name, channel_id):
        self.bot_id = bot_id
        self.name = name
        self.channel_id = channel_id

    def __str__(self):
        return f"TrashBot: {self.name} with id: {self.bot_id}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.bot_id == other.bot_id

    def __hash__(self):
        return hash(self.bot_id)

    def get_name(self) -> str:
        """TrashBot name :return: str"""
        return self.name

    def get_id(self) -> str:
        """TrashBot id :return: str"""
        return self.bot_id

    def set_id(self, bot_id: str):
        self.bot_id = bot_id

    def set_name(self, name: str):
        self.name = name

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

    def random_dont_understand(self) -> str:
        """TrashBot random dont understand :return: str"""
        return random.choice(TRASH_BOT_DONT_UNDERSTAND)

    def not_found_link(self) -> str:
        """TrashBot already exists message :return: str"""
        return TRASH_BOT_NOT_FOUND_LINK

    def new_video_added(self) -> str:
        """TrashBot new video event response :return: str"""
        return random.choice(TRASH_BOT_NEW_VIDEO_ADDED)

    def generate_bot_post_to_channel(self, sender_user_id: str, video_db_row: dict, message=None) -> str:
        """TrashBot post message to channel with message or without
        :param video_db_row: video row from db
        :param sender_user_id: the user who sent the message
        :param message: the message that the user sent
        :return: str
        """
        video_reply_text = self.get_reply_text_from_video_row(video_db_row=video_db_row)
        if message:
            return f"<@{sender_user_id}> just requested a trash video! \n\nMessage: \"{message}\".\n\n {video_reply_text}"
        return f"<@{sender_user_id}> just requested a trash video!\n {video_reply_text}"

    def generate_bot_challenge_post_to_channel(self, challenge: dict) -> str:
        """TrashBot post message to challenge to channel
        :param challenge: the challenge that the user sent
        :return: str
        """
        challenge_title = challenge.get('title', '')
        challenge_type = challenge.get('type', '')
        challenge_text = challenge.get('challenge', '')
        trashbot_challenge_text = random.choice(TRASH_BOT_CHALLENGE_TITLE)
        challenge_emoji = ':thought_balloon:' if challenge_type == 'text' else ':frame_with_picture:'
        return f"This week challenge just arrived! \n\n :star2: *[{challenge_title}]* :star2:\n\n" \
               f"_{challenge_text}_\n\n" \
               f"Post your {challenge_emoji} in this thread and we will vote for the best one!"

    def generate_dm_text(self, recipient_user_id: str, sender_user_id: str, video_db_row: dict, message=None) -> str:
        """TrashBot reply with message for messaging functionality
        :param video_db_row: video row from db
        :param sender_user_id: the user who sent the message
        :param message: the message that the user sent
        :param recipient_user_id: the user who will receive the message
        :return: str
        """
        video_reply_text = self.get_reply_text_from_video_row(video_db_row=video_db_row)
        if message:
            return f"Hey <@{recipient_user_id}>! <@{sender_user_id}> just sent a trash video for you! \n\nMessage: \"{message}\".\n\n {video_reply_text}"
        return f"Hey <@{recipient_user_id}>! <@{sender_user_id}> just sent a trash video for you!\n {video_reply_text}"

    def get_reply_text_from_video_row(self, video_db_row: dict or None) -> str:
        """TrashBot reply with message for messaging functionality"""
        return f"video #{video_db_row['id']} https://www.youtube.com/watch?v={video_db_row['video_id']} video rating: {video_db_row['rating']} /5 "

    def ask_for_introduction(self, user_name) -> str:
        """TrashBot ask for introduction message :return: str"""
        return f"Welcome to the random channel, <@{user_name}>! 🎉 You should introduce yourself to the rest of the team with an energizing trash video. 🎉"

    def get_emoji_event_response(self, emoji_name) -> str:
        """TrashBot emoji event response :return: str"""
        return random.choice(TRASH_BOT_EMOJI_REPLIES) + f" -> :{emoji_name}:"

    def help(self) -> str:
        """TrashBot help message :return: str"""
        return TRASHBOT_HELP_MSG

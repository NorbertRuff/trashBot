import logging
import re
from datetime import datetime

YOUTUBE_URL_REGEX = ('(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})')


def make_new_timestamp():
    return datetime.now()


def user_is_bot_or_app_mention(user, text, bot_id):
    """Check if the user is the bot"""
    user_is_bot = user == bot_id or text.startswith(f"<@{bot_id}>")
    logging.getLogger().warning(f"user_is_bot: {user_is_bot}")
    return user_is_bot


def match_youtube_url(text):
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    if youtube_regex_match:
        return youtube_regex_match.group(1)
    return None

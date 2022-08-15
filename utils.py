import logging
import re
from datetime import datetime
import random

YOUTUBE_URL_REGEX = ('(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})')


def make_new_timestamp():
    return datetime.now()


def user_is_bot(user, bot_id):
    """Check if the user is the bot"""
    return user == bot_id


def get_random_from_playlist(playlist):
    """Get a random trash video"""
    random_number = random.randint(0, len(playlist) - 1)
    video_id = playlist[random_number]['video_id']
    return f'https://www.youtube.com/watch?v={video_id}'


def match_youtube_url(text):
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    if youtube_regex_match:
        return youtube_regex_match.group(1)
    return None

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
    return video_id


def match_youtube_url(text):
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    if youtube_regex_match:
        return youtube_regex_match.group(1)
    return None


def get_rating_section(video_id):
    """Get the rating section of a video"""
    rate_block = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "How painful is this video? Rate it!"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "1"
                        },
                        "style": "danger",
                        "value": f"{video_id} 1"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "2"
                        },
                        "value": f"{video_id} 2"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "3"
                        },
                        "value": f"{video_id} 3"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "4"
                        },
                        "value": f"{video_id} 4"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "5"
                        },
                        "style": "primary",
                        "value": f"{video_id} 5"
                    }
                ]
            }
        ]
    }
    return rate_block

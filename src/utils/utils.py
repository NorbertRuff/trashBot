import re
from datetime import datetime
from psycopg2.extras import RealDictRow
import random

from src import utils, data_manager
from src.bot import TrashBot

YOUTUBE_URL_REGEX = ('(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})')


def make_new_timestamp() -> datetime:
    """Make a new timestamp"""
    return datetime.now()


def user_is_bot(user: str, bot_id: str) -> bool:
    """Check if the user is the bot"""
    return user == bot_id


def get_random_video_from_db() -> str or None:
    """Get a random video id from the playlist"""
    playlist = data_manager.get_all_videos()
    video = utils.get_random_video_from_playlist(playlist)
    return video if video else None


def get_random_video_response(say, bot: TrashBot) -> str or None:
    """Get a random video from the playlist with message or error message"""
    playlist = data_manager.get_all_videos()
    video = utils.get_random_video_from_playlist(playlist)
    if video:
        say(f"{bot.random_general_reply()} video #{video['id']} https://www.youtube.com/watch?v={video['video_id']} video rating: {video['rating']} /5 ")
        say(utils.get_rating_section(video['video_id']))
        return None
    return bot.general_error_reply()


def get_random_video_from_playlist(playlist: list) -> RealDictRow:
    """Get a random trash video"""
    random_number = random.randint(0, len(playlist) - 1)
    video = playlist[random_number]
    return video


def match_youtube_url(text: str) -> str or None:
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    if youtube_regex_match:
        return youtube_regex_match.group(1)
    return None


def get_rating_section(video_id: str) -> dict:
    """Get the rating section interactive block section for a video"""
    rate_block = {
        "text": "How painful is this video? Rate it from 1 to 5",
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
                        "value": f"{video_id} 1",
                        "action_id": "rate_video_1",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "2"
                        },
                        "value": f"{video_id} 2",
                        "action_id": "rate_video_2",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "3"
                        },
                        "value": f"{video_id} 3",
                        "action_id": "rate_video_3",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "4"
                        },
                        "value": f"{video_id} 4",
                        "action_id": "rate_video_4",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "5"
                        },
                        "style": "primary",
                        "value": f"{video_id} 5",
                        "action_id": "rate_video_5",
                    }
                ]
            }
        ]
    }
    return rate_block

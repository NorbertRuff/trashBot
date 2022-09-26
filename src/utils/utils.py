import logging
import random
import re
from datetime import datetime

from psycopg2.extras import RealDictRow
from slack_bolt import Say

from src import data_manager
from src.slack_bot import TrashBot, TRASH_BOT_ALREADY_IN_PLAYLIST, TRASH_BOT_VIDEO_ADDED, TRASH_BOT_NOT_FOUND_LINK
from src.utils import blocks
from src.utils.youtube import get_youtube_video_info

YOUTUBE_URL_REGEX = (
    '(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})')


def make_new_timestamp() -> datetime:
    """Make a new timestamp"""
    return datetime.now()


def user_is_bot(user: str, bot_id: str) -> bool:
    """Check if the user is the slackBot"""
    return user == bot_id


def get_random_video_db_row() -> str or None:
    """Returns a random video id from the playlist"""
    playlist = data_manager.get_all_videos()
    video_db_row = get_random_video_db_row_from_playlist(playlist)
    return video_db_row if video_db_row else None


def save_video(text: str, user_id: str, bot: TrashBot) -> str:
    """Save a video to the playlist"""
    video_id = match_youtube_url(text)
    youtube_data = get_youtube_video_info(video_id)
    if not video_id or not youtube_data:
        return TRASH_BOT_NOT_FOUND_LINK
    try:
        if data_manager.video_exists(video_id)['exists']:
            return f'{bot.random_error_reply()} {TRASH_BOT_ALREADY_IN_PLAYLIST} video id:{video_id}'
        data_manager.put_video_in_table(video_id=video_id, user_id=user_id, fallback=youtube_data['title'],
                                        title=youtube_data['title'],
                                        author_name=youtube_data['author_name'])
        return f'{bot.random_success_reply()} {TRASH_BOT_VIDEO_ADDED}'
    except Exception as e:
        logging.error(e)
        return bot.general_error_reply()


def get_random_video_response(say: Say, bot: TrashBot) -> str or None:
    """Returns a random video from the playlist with message or error message"""
    video_db_row = get_random_video_db_row()
    if video_db_row:
        say(f"{bot.random_general_reply()} video #{video_db_row['id']} https://www.youtube.com/watch?v={video_db_row['video_id']} video rating: {video_db_row['rating']} /5 ")
        say(blocks.get_rating_section(video_db_row['video_id']))
        return None
    return bot.general_error_reply()


def get_random_video_db_row_from_playlist(playlist: list) -> RealDictRow:
    """Returns a random trash video"""
    random_number = random.randint(0, len(playlist) - 1)
    video_db_row = playlist[random_number]
    return video_db_row


def match_youtube_url(text: str) -> str or None:
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    if youtube_regex_match:
        return youtube_regex_match.group(1)
    return None

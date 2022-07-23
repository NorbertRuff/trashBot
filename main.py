import logging
import os
import random
import re

from dotenv import load_dotenv
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from bot_messages import TRASHBOT_HELP_MSG, TRASH_BOT_GENERAL_REPLIES, TRASH_BOT_SHIT_HIT_THE_FAN, TRASH_BOT_LOVE, \
    TRASH_BOT_HATE, \
    TRASH_BOT_DONT_UNDERSTAND, MESSAGE_BLOCK, TRASH_BOT_NOT_FOUND_LINK, \
    TRASH_BOT_SUCCESS_REPLIES, TRASH_BOT_ERROR_REPLIES, TRASH_BOT_ALREADY_IN_PLAYLIST, TRASH_BOT_VIDEO_ADDED, \
    TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS, TRASH_BOT_UPLOAD_LAST_VALID_URL_KEYWORDS, TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS, \
    TRASH_BOT_PLAYLIST
from youtube_service import get_yt_playlist, insert_video_to_youtube_playlist

load_dotenv()
app = Flask(__name__)

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]

slack_web_client = WebClient(token=SLACK_BOT_TOKEN)
slack_event_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)

YOUTUBE_URL_REGEX = ('(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})')

LAST_YOUTUBE_LINK_DETAILS = {
    'message': None,
    'video_id': None,
}


def video_is_in_playlist(video_id):
    """Check if a video is in the playlist"""
    return video_id in [item['contentDetails']['videoId'] for item in get_yt_playlist()['items']]


def handle_bot_command(text):
    """Handle a bot commands"""
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS):
        video = get_random_from_playlist()
        if video:
            return f'{random.choice(TRASH_BOT_GENERAL_REPLIES)} {video}'
        return TRASH_BOT_SHIT_HIT_THE_FAN
    if any(word in text.lower() for word in [':point_right:']) and any(word in text.lower() for word in TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS):
        video_id = match_youtube_url(text)
        return try_to_save_video(video_id)
    if any(word in text.lower() for word in [':point_up:', ':point_up_2:']) and any(word in text.lower() for word in TRASH_BOT_UPLOAD_LAST_VALID_URL_KEYWORDS):
        video_id = LAST_YOUTUBE_LINK_DETAILS['video_id']
        return try_to_save_video(video_id)
    if "playlist" in text.lower():
        return f'{TRASH_BOT_GENERAL_REPLIES[1]} {TRASH_BOT_PLAYLIST}'
    if "last" in text.lower():
        if LAST_YOUTUBE_LINK_DETAILS['video_id']:
            return f'{random.choice(TRASH_BOT_GENERAL_REPLIES)} https://www.youtube.com/watch?v={LAST_YOUTUBE_LINK_DETAILS["video_id"]}'
        return f'{random.choice(TRASH_BOT_ERROR_REPLIES)} No video found'
    if "good bot" in text.lower():
        return TRASH_BOT_LOVE
    if "bad bot" in text.lower():
        return TRASH_BOT_HATE
    return TRASH_BOT_DONT_UNDERSTAND


def try_to_save_video(video_id):
    """Try to save a video to the playlist"""
    try:
        if not video_id:
            return TRASH_BOT_NOT_FOUND_LINK
        if video_is_in_playlist(video_id):
            return f'{random.choice(TRASH_BOT_ERROR_REPLIES)} {TRASH_BOT_ALREADY_IN_PLAYLIST} video id:{video_id}'
        response = insert_video_to_youtube_playlist(video_id)
        if response == "success":
            return f'{random.choice(TRASH_BOT_SUCCESS_REPLIES)} {TRASH_BOT_VIDEO_ADDED}'
        return TRASH_BOT_SHIT_HIT_THE_FAN
    except Exception as e:
        logging.error(e)
        return TRASH_BOT_SHIT_HIT_THE_FAN


def get_random_from_playlist():
    """Get a random trash video"""
    try:
        playlist = get_yt_playlist()
        random_number = random.randint(0, len(playlist['items']) - 1)
        video_id = playlist['items'][random_number]['contentDetails']['videoId']
    except Exception as e:
        logging.error(e)
        return None
    return f'https://www.youtube.com/watch?v={video_id}'


def match_youtube_url(text):
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    if youtube_regex_match:
        return youtube_regex_match.group(1)
    return None


@slack_event_adapter.on("app_mention")
def handle_message(payload):
    """Handle message event"""
    event = payload.get("event", {})
    text = event.get("text", "")
    channel = event.get("channel", "")
    message = handle_bot_command(text)
    MESSAGE_BLOCK["text"]["text"] = message
    message_to_send = {"channel": channel, "blocks": [MESSAGE_BLOCK]}
    return slack_web_client.chat_postMessage(**message_to_send)


@slack_event_adapter.on("message")
def handle_message(payload):
    """Handle messages sent to the bot"""
    event = payload.get("event", {})
    text = event.get("text", "")
    user = event.get("user", "")
    match = match_youtube_url(text)
    if match:
        LAST_YOUTUBE_LINK_DETAILS['video_id'] = match
        LAST_YOUTUBE_LINK_DETAILS['message'] = text
        LAST_YOUTUBE_LINK_DETAILS['user'] = user


if __name__ == "__main__":
    app.run(debug=True, port=os.environ.get('PORT', 3000))

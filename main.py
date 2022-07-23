import os
import random
import re
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from botMessages import TRASHBOT_HELP_MSG, TRASH_BOT_REPLIES, TRASH_BOT_SHIT_HIT_THE_FAN, TRASH_BOT_LOVE, \
    TRASH_BOT_HATE, \
    TRASH_BOT_DONT_UNDERSTAND, MESSAGE_BLOCK, TRASH_BOT_NOT_FOUND_LINK, TRASH_BOT_NOT_PREVIOUS_LINK, \
    TRASH_BOT_SUCCESS_REPLIES

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
PLAYLIST_ID = os.environ["PLAYLIST_ID"]
scopes = [os.environ["SCOPE"]]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]
YOUTUBE_CLIENT_SECRETS_FILE = "client_secret_1092500365377-73nfre97br2l69v5n8e6l9gb6u32hjt7.apps.googleusercontent.com.json"
YOUTUBE_MISSING_SECRETS_MSG = "Missing Youtube client secrets"

app = Flask(__name__)

slack_web_client = WebClient(token=SLACK_BOT_TOKEN)
slack_event_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)

YOUTUBE_URL_REGEX = ('(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})')

LAST_YOUTUBE_LINK_DETAILS = {
    'message': None,
    'video_id': None,
    'rating': None,
}


def handle_bot_command(text):
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in ['random', 'get', 'surprise', 'get a random', 'trash', 'trash video', 'random video']):
        video = get_random_from_playlist()
        if video:
            return f'{random.choice(TRASH_BOT_REPLIES)} {video}'
        return TRASH_BOT_SHIT_HIT_THE_FAN
    if any(word in text.lower() for word in [':point_right:', 'save', 'add', 'add to', 'add to playlist', 'add to trash']):
        print(text)
        try:
            video_id = match_youtube_url(text)
            if not video_id:
                return TRASH_BOT_NOT_FOUND_LINK
            response = save_video_to_playlist(video_id)
            if response == "success":
                return f'{random.choice(TRASH_BOT_SUCCESS_REPLIES)} Video added to trash playlist'
            return TRASH_BOT_SHIT_HIT_THE_FAN
        except Exception as e:
            return TRASH_BOT_SHIT_HIT_THE_FAN
    if any(word in text.lower() for word in [':point_up:', ':point_up_2:']) and any(word in text.lower() for word in ['save', 'playlist']):
        if not LAST_YOUTUBE_LINK_DETAILS['video_id']:
            return TRASH_BOT_NOT_PREVIOUS_LINK
        try:
            response = save_video_to_playlist(video_id=LAST_YOUTUBE_LINK_DETAILS['video_id'])
            if response == "success":
                return f'{random.choice(TRASH_BOT_SUCCESS_REPLIES)} Video added to trash playlist'
            return TRASH_BOT_SHIT_HIT_THE_FAN
        except Exception as e:
            return TRASH_BOT_SHIT_HIT_THE_FAN
    if "good bot" in text.lower():
        return TRASH_BOT_LOVE
    if "bad bot" in text.lower():
        return TRASH_BOT_HATE
    return TRASH_BOT_DONT_UNDERSTAND


def get_authenticated_service():
    """
    Returns an instance of an Authenticated YouTube service object.
    """
    if os.path.exists("CREDENTIALS_PICKLE_FILE"):
        with open("CREDENTIALS_PICKLE_FILE", 'rb') as f:
            credentials = pickle.load(f)
    else:

        credentials = ser
        with open("CREDENTIALS_PICKLE_FILE", 'wb') as f:
            pickle.dump(credentials, f)
    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)


def save_video_to_playlist(video_id):
    """Save a video to the trash playlist"""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = get_authenticated_service()
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": PLAYLIST_ID,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id,
                },
            },
        },
    )
    response = request.execute()
    if response["snippet"]["playlistId"] == PLAYLIST_ID:
        return "success"
    return "failure"


def get_yt_playlist():
    """Get the trash video playlist"""
    youtube = get_authenticated_service()
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=100,
        playlistId=PLAYLIST_ID,
    )
    response = request.execute()
    print(response)
    return response


def get_random_from_playlist():
    """Get a random trash video"""
    try:
        playlist = get_yt_playlist()
        random_number = random.randint(0, len(playlist['items']) - 1)
        video_id = playlist['items'][random_number]['contentDetails']['videoId']
    except Exception as e:
        return None
    return f'https://www.youtube.com/watch?v={video_id}'


def match_youtube_url(text):
    """Match a YouTube URL"""
    youtube_regex_match = re.search(YOUTUBE_URL_REGEX, text)
    print(youtube_regex_match)
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
    print(f"Received message: {text}")
    print(LAST_YOUTUBE_LINK_DETAILS)


if __name__ == "__main__":
    app.run(debug=True, port=os.environ.get('PORT', 3000))

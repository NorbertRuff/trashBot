import os
import random
import re

from flask import Flask
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
from slack import WebClient
from slackeventsapi import SlackEventAdapter

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
PLAYLIST_ID = os.environ["PLAYLIST_ID"]
scopes = [os.environ["SCOPE"]]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRET_FILE = ""

app = Flask(__name__)

slack_web_client = WebClient(token=SLACK_BOT_TOKEN)
slack_event_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)

TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

Mention me in a message and I can do the following: 
    @trashbot help -> Print this message
    @trashbot random trash -> I will get a random trash for you
    @trashbot :point_up: save -> I will save the video from the previous post to the trash playlist
    @trashbot :point_right: save videoUrl ->  I will save the video in this message to the trash playlist

The trash playlist is here:
    https://www.youtube.com/playlist?list={PLAYLIST_ID}
    
You can check out my source code here:
    https://github.com/NorbertRuff/trashBot
"""

MESSAGE_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    },
}

TRASHBOT_REPLIES = ['This is a classic -> ', 'Biip-bop-bup -> ', 'Voila! -> ', 'I love trash -> ', 'just for you -> ']
TRASHBOT_LOVE = 'WOW thanks :heart_eyes: I Love you'
TRASHBOT_HATE = ':cry: sorry, I hate you'
TRASHBOT_NOT_FOUND = 'Huh? I did not understand that'
TRASHBOT_SHIT_HIT_THE_FAN = 'Something went wrong, I hit the fan'

"""
Regular expressions to capture the YouTube video Id
"""
YOUTUBE_URL_REGEX = ('<(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?>')
last_yt_url = ""
# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


def handle_bot_command(text):
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in ['random', 'get', 'surprise', 'get a random']) and any(word in text.lower() for word in ['trash', 'video']):
        video = get_random_from_playlist()
        if video:
            return f'{random.choice(TRASHBOT_REPLIES)} {video}'
        return TRASHBOT_SHIT_HIT_THE_FAN
    if ':point_right: save' in text.lower():
        try:
            video_id = match_youtube_url(text)
            save_video_to_playlist(video_id)
            return f'{random.choice(TRASHBOT_REPLIES)} Video added to trash playlist'
        except Exception as e:
            return TRASHBOT_SHIT_HIT_THE_FAN
    if any(word in text.lower() for word in [':point_up: save', ':point_up_2: save']):
        try:
            save_video_to_playlist(last_yt_url)
            return f'{random.choice(TRASHBOT_REPLIES)} Video added to trash playlist'
        except Exception as e:
            return TRASHBOT_SHIT_HIT_THE_FAN
    if "good bot" in text.lower():
        return TRASHBOT_LOVE
    if "bad bot" in text.lower():
        return TRASHBOT_HATE
    return TRASHBOT_NOT_FOUND


def save_video_to_playlist(video_id):
    """Save a video to the trash playlist"""
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
    print(response)
    return response


def get_yt_playlist():
    """Get the trash video playlist"""
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

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
    match = match_youtube_url(text)
    if match:
        global last_yt_url
        last_yt_url = match


if __name__ == "__main__":
    app.run(debug=True, port=os.environ.get('PORT', 3000))

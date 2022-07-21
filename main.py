import logging
import os
import random
import re

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


load_dotenv()
logging.basicConfig(level=logging.DEBUG)

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

PLAYLIST_ID = os.environ["PLAYLIST_ID"]
scopes = [os.environ["SCOPE"]]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRET_FILE = "YOUR_CLIENT_SECRET_FILE.json"

app = App(token=SLACK_BOT_TOKEN, name="Trash Bot")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

"""
Regular expressions to capture the YouTube video Id
"""
YOUTUBE_URL_PATTERNS = [
    re.compile(r'^http(?:s)??:\/\/(?:www\.)??youtube\.com/watch\?v=(?P<v>[\w\-_]+)'),
    re.compile(r'^http(?:s)??:\/\/(?:www\.)??youtu.be/(?P<v>[\w\-_]+)'),
]

TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

I can do the following: 
    help - Print this message
    get-a-random-trash - I will get a random trash for you
    save - I will save the video to your trash playlist

The trash playlist is here:
    https://www.youtube.com/playlist?list={PLAYLIST_ID}
"""

TRASHBOT_REPLIES = ['This is an classic -> ', 'Biip-bop-bup -> ', 'Voila! -> ', 'I am trash -> ', 'just for you -> ']
TRASHBOT_LOVE = 'WOW thanks :heart_eyes: I Love you'
TRASHBOT_HATE = ':cry: sorry, I\'ll try to improve myself'
TRASHBOT_NOT_FOUND = 'Huh? I did not understand that'
TRASHBOT_SHIT_HIT_THE_FAN = 'Something went wrong, I hit the fan'


def save_video_to_playlist(text):
    pass


def handle_bot_command(text):
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in ['random', 'get', 'surprise', 'get a random']):
        video = get_random_from_playlist()
        return f'{random.choice(TRASHBOT_REPLIES)} {video}'
    if any(word in text.lower() for word in ['put in playlist', 'save', 'save video']):
        try:
            video = match_youtube_url(text)['v']
            save_video_to_playlist(video)
            return f'{random.choice(TRASHBOT_REPLIES)} Video added to trash playlist'
        except Exception as e:
            logging.error(e)
            return TRASHBOT_SHIT_HIT_THE_FAN
    if "good bot" in text.lower():
        return TRASHBOT_LOVE
    if "bad bot" in text.lower():
        return TRASHBOT_HATE
    return TRASHBOT_NOT_FOUND


@app.event(event="app_mention")
def handle_mention(payload, say, logger):
    """Handle app mention event"""
    text = payload["text"]
    print(text)
    result = handle_bot_command(text)
    say(text=result)


@app.event(event="link_shared")
def event_link(payload, say, logger):
    """Handle link shared event"""
    print(payload['links'][0])
    logger.info(payload)
    say("link?")


@app.event("message")
def handle_message_events(payload, logger):
    """Handle message event"""
    print(payload)
    logger.info(payload)


@app.command("/get-a-random-trash")
def get_random_trash(ack, payload, logger):
    """get random trash video"""
    logger.info(payload)
    ack(get_random_from_playlist())


@app.command("/save")
def save_trash(ack, payload, logger):
    """Handle save event"""
    text = payload["text"]
    if not text:
        ack("Please provide a video url")
        return
    logger.info(payload)
    ack(save_video_to_playlist(text))


@app.command("/help")
def handle_help(ack, payload, logger):
    """Handle help event"""
    logger.info(payload)
    ack(TRASHBOT_HELP_MSG)


def get_random_from_playlist():
    """Get a random trash video"""
    try:
        playlist = get_yt_playlist()
        random_number = random.randint(0, len(playlist['items']) - 1)
        video_id = playlist['items'][random_number]['contentDetails']['videoId']
    except Exception as e:
        logging.error(e)
        return TRASHBOT_SHIT_HIT_THE_FAN
    return f'https://www.youtube.com/watch?v={video_id}'


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


def match_youtube_url(url):
    """Match a YouTube URL"""
    for pattern in YOUTUBE_URL_PATTERNS:
        match = pattern.match(url)
        if match:
            return match.groupdict()
    return None


def get_yt_playlist():
    """Get the trash video playlist"""
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes)
    credentials = flow.run_console()
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


if __name__ == "__main__":
    main()

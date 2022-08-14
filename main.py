import random
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from bot_messages import *
import logging
import data_manager
import utils
from flask import Flask, request
load_dotenv()

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
TRASH_CHANNEL_ID = os.environ["TRASH_CHANNEL_ID"]
app = App(token=SLACK_BOT_TOKEN)

flask_app = Flask(__name__)
handler = SocketModeHandler(app, SLACK_APP_TOKEN).start()
logging.basicConfig(level=logging.DEBUG)

BOT_ID = app.client.auth_test()["user_id"]


LAST_YOUTUBE_LINK_DETAILS = {
    'message': None,
    'video_id': None,
}


def handle_event_text(text, user):
    """Handle a bot commands"""
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS):
        playlist = data_manager.get_all_videos()
        video = get_random_from_playlist(playlist)
        if video:
            return f'{random.choice(TRASH_BOT_GENERAL_REPLIES)} {video}'
        return TRASH_BOT_SHIT_HIT_THE_FAN
    if any(word in text.lower() for word in [':point_right:']) and any(
            word in text.lower() for word in TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS):
        video_id = utils.match_youtube_url(text)
        return save_video(video_id, user)
    if "good bot" in text.lower():
        return random.choice(TRASH_BOT_LOVE)
    if "bad bot" in text.lower():
        return random.choice(TRASH_BOT_HATE)
    return TRASH_BOT_DONT_UNDERSTAND


def save_video(video_id, user):
    """Save a video to the playlist"""
    try:
        if not video_id:
            return TRASH_BOT_NOT_FOUND_LINK
        video_exist = data_manager.video_exists(video_id)
        if video_exist['exists']:
            return f'{random.choice(TRASH_BOT_ERROR_REPLIES)} {TRASH_BOT_ALREADY_IN_PLAYLIST} video id:{video_id}'
        data_manager.put_video_in_table(video_id, user)
        return f'{random.choice(TRASH_BOT_SUCCESS_REPLIES)} {TRASH_BOT_VIDEO_ADDED}'
    except Exception as e:
        logging.error(e)
        return TRASH_BOT_SHIT_HIT_THE_FAN


def get_random_from_playlist(playlist):
    """Get a random trash video"""
    random_number = random.randint(0, len(playlist) - 1)
    video_id = playlist[random_number]['video_id']
    return f'https://www.youtube.com/watch?v={video_id}'


@app.message("hello")
def handle_hello(message, say):
    """Handle hello message"""
    user = message.get("user", "")
    say(f"Hello! <@{user}> :wave:")


@app.event("message")
def handle_message_events(body, event, logger):
    """Handle message events"""
    text = event.get("text", "")
    user = event.get("user", "")
    if utils.user_is_bot_or_app_mention(user, text, BOT_ID):
        return
    # logger.info(body)
    match = utils.match_youtube_url(text)
    if match:
        print(match)
        LAST_YOUTUBE_LINK_DETAILS['video_id'] = match
        LAST_YOUTUBE_LINK_DETAILS['message'] = text
        LAST_YOUTUBE_LINK_DETAILS['user'] = user


# <------------------------events------------------------------->
@app.event("app_mention")
def handle_bot_mention(body, event, say, logger):
    """Handle bot mention"""
    logger.info(body)
    text = event.get("text", "")
    user = event.get("user", "")
    channel = event.get("channel", "")
    message = handle_event_text(text, user)
    say(message)


@app.event("emoji_changed")
def handle_emoji_changed_events(event, say, logger):
    """Handle emoji changed events"""
    logger.info(event)
    text = event.get("text", "")
    user = event.get("user", "")
    print(event)
    say(f"Its not really my job, but you should know that an emoji has been changed :{event}:")


@app.event("team_join")
def ask_for_introduction(event, say, logger):
    """When new user joins channel asks for introduction"""
    logger.info(event)
    text = event.get("text", "")
    user = event.get("user", "")
    text = f"Welcome to the team, <@{user}>! 🎉 You can introduce yourself in this channel with a greeting trash video."
    say(text=text)


# <------------------------command------------------------------->
@app.command("/help")
def handle_help_command(ack, body, respond, logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    ack()
    respond(TRASHBOT_HELP_MSG)


@app.command("/list")
def handle_list_command(ack, body, respond, logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    playlist = data_manager.get_all_videos()
    response = ""
    for video in playlist:
        response += f'#{video["id"]} -> https://www.youtube.com/watch?v={video["video_id"]}\n'
    ack()
    respond(response)


@app.command("/add")
def handle_add_command(ack, body, respond, logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    link = body.get("text", "")
    user_id = body.get("user_id", "")
    video_id = utils.match_youtube_url(link)
    ack()
    if video_id:
        response = save_video(video_id, user_id)
        respond(response)
    respond(random.choice(TRASH_BOT_ERROR_REPLIES))


# <------------------------shortcut------------------------------->
@app.shortcut("save_shortcut")
def handle_shortcut_save(ack, body, respond, logger):
    """Save a video to the playlist"""
    message = body.get("message", "")
    text = message.get("text", "")
    user = body.get("user", "")
    user_id = user.get("id", "")
    video_id = utils.match_youtube_url(text)
    ack()
    if video_id:
        response = save_video(video_id, user_id)
        respond(response)
    respond(random.choice(TRASH_BOT_ERROR_REPLIES))


@app.error
def custom_error_handler(error, body, logger):
    """Custom error handler"""
    logger.exception(f"Error: {error}")
    # logger.info(f"Request body: {body}")


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Start your app
# if __name__ == "__main__":
#     handler = SocketModeHandler(app, SLACK_APP_TOKEN)
#     handler.start()

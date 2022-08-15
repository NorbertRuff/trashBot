import random
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from bot import TrashBot
from bot_messages import *
import logging
import data_manager
import utils

load_dotenv()

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
TRASH_CHANNEL_ID = os.environ["TRASH_CHANNEL_ID"]
app = App(token=SLACK_BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

BOT_ID = app.client.auth_test()["user_id"]
BOT_NAME = app.client.auth_test()["user"]
BOT = TrashBot(BOT_ID, BOT_NAME)
logging.getLogger().warning(f"BOT_ID: {BOT_ID}")

LAST_YOUTUBE_LINK_DETAILS = {
    'message': None,
    'video_id': None,
}


def handle_event_text(text, user):
    """Handle a bot commands"""
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS):
        return get_random_video_response()
    if any(word in text.lower() for word in [':point_right:']) and any(
            word in text.lower() for word in TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS):
        return save_video(text, user)
    if "good bot" in text.lower():
        return BOT.random_love_reply()
    if "bad bot" in text.lower():
        return BOT.random_hate_reply()
    return TRASH_BOT_DONT_UNDERSTAND


def get_random_video_response():
    """Get a random video from the playlist with message or error message"""
    playlist = data_manager.get_all_videos()
    video = utils.get_random_from_playlist(playlist)
    if video:
        return f'{BOT.random_general_reply()} {video}'
    return TRASH_BOT_SHIT_HIT_THE_FAN


def save_video(text, user):
    """Save a video to the playlist"""
    video_id = utils.match_youtube_url(text)
    if not video_id:
        return TRASH_BOT_NOT_FOUND_LINK
    try:
        if data_manager.video_exists(video_id)['exists']:
            return f'{BOT.random_error_reply()} {TRASH_BOT_ALREADY_IN_PLAYLIST} video id:{video_id}'
        data_manager.put_video_in_table(video_id, user)
        return f'{BOT.random_success_reply()} {TRASH_BOT_VIDEO_ADDED}'
    except Exception as e:
        logging.error(e)
        return TRASH_BOT_SHIT_HIT_THE_FAN


# <------------------------message------------------------------->
@app.message("hello")
def handle_hello(message, ack, say, logger):
    """Handle hello message"""
    user = message.get("user", "")
    ack()
    logger.info(message)
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.say_hi_to(user))


def return_random_video(video, say):
    say(BOT.random_general_reply())
    say(video)
    say(TRASH_BOT_RATE)
    
    
# <------------------------events------------------------------->
@app.event("message")
def handle_message_events(message, ack, event, logger):
    """Handle message events"""
    text = event.get("text", "")
    user = message.get("user", "")
    logger.info(message)
    ack()
    if utils.user_is_bot(user, BOT_ID):
        return
    match = utils.match_youtube_url(text)
    if match:
        logger.info(f"Matched youtube link: {match}")
        LAST_YOUTUBE_LINK_DETAILS['video_id'] = match
        LAST_YOUTUBE_LINK_DETAILS['message'] = text
        LAST_YOUTUBE_LINK_DETAILS['user'] = user


@app.event("app_mention")
def handle_bot_mention(body, ack, event, say, logger):
    """Handle bot mention"""
    logger.info(body)
    ack()
    text = event.get("text", "")
    user = event.get("user", "")
    message = handle_event_text(text, user)
    say(message)


@app.event("emoji_changed")
def handle_emoji_changed_events(event, say, logger):
    """Handle emoji changed events"""
    logger.info(event)
    text = event.get("text", "")
    user = event.get("user", "")
    say(f"Its not really my job, but you should know that an emoji has been changed :{event}:")


@app.event("team_join")
def ask_for_introduction(event, say, logger):
    """When new user joins channel asks for introduction"""
    logger.info(event)
    text = event.get("text", "")
    user = event.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
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
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    ack()
    response = save_video(text, user_id)
    respond(response)


# <------------------------shortcuts------------------------------->
@app.shortcut("save_shortcut")
def handle_shortcut_save(ack, body, respond, logger):
    """Save a video to the playlist"""
    message = body.get("message", "")
    text = message.get("text", "")
    user = body.get("user", "")
    user_id = user.get("id", "")
    ack()
    response = save_video(text, user_id)
    respond(response)


@app.error
def custom_error_handler(error, body, logger):
    """Custom error handler"""
    logger.exception(f"Error: {error}")
    logger.info(f"Request body: {body}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

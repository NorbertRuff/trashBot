import os
import re

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from src.bot import *
from src.bot.bot import TrashBot
import logging

from src.data_manager import data_manager
from src.utils import utils

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
    'title': None,
    'thumb_url': None,
    'video_id': None,
    'video_html': None,
    'user': None,
}


def handle_event_text(text: str, user: str, say: str) -> str:
    """Handle a bot commands"""
    if "help" in text.lower():
        return TRASHBOT_HELP_MSG
    if any(word in text.lower() for word in TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS):
        return get_random_video_response(say)
    if any(word in text.lower() for word in TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS):
        return save_video(text, user)
    if "good bot" in text.lower():
        return BOT.random_love_reply()
    if "bad bot" in text.lower():
        return BOT.random_hate_reply()
    if "source code" in text.lower():
        return 'https://github.com/NorbertRuff/trashBot'
    return TRASH_BOT_DONT_UNDERSTAND


def get_random_video() -> str or None:
    """Get a random video id from the playlist"""
    playlist = data_manager.get_all_videos()
    video = utils.get_random_video_from_playlist(playlist)
    if video:
        return f"video #{video['id']} https://www.youtube.com/watch?v={video['video_id']} video rating: {video['rating']} /5 "
    return None


def get_random_video_response(say):
    """Get a random video from the playlist with message or error message"""
    playlist = data_manager.get_all_videos()
    video = utils.get_random_video_from_playlist(playlist)
    if video:
        say(f"{BOT.random_general_reply()} video #{video['id']} https://www.youtube.com/watch?v={video['video_id']} video rating: {video['rating']} /5 ")
        say(utils.get_rating_section(video['video_id']))
        return None
    return TRASH_BOT_SHIT_HIT_THE_FAN


def save_video(text: str, user: str) -> str:
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
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.say_hi_to(user))


@app.message("good bot")
def handle_bot_love(message, ack, say, logger):
    """Handle hello message"""
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.random_love_reply())


@app.message("bad bot")
def handle_bot_hate(message, ack, say, logger):
    """Handle hello message"""
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.random_hate_reply())


# <------------------------events------------------------------->
@app.event("message")
def handle_message_events(message, ack, event, logger):
    """Handle message events"""
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    # attachment = message["message"]["attachments"][0] if "message" in message and "attachments" in message["message"] else None
    # if attachment:
    #     match = utils.match_youtube_url(attachment.get("from_url", ""))
    #     if match:
    #         LAST_YOUTUBE_LINK_DETAILS['video_id'] = match
    #         LAST_YOUTUBE_LINK_DETAILS['title'] = attachment.get("title", "")
    #         LAST_YOUTUBE_LINK_DETAILS['thumb_url'] = attachment.get("thumb_url", "")
    #         LAST_YOUTUBE_LINK_DETAILS['user'] = user
    #         LAST_YOUTUBE_LINK_DETAILS['video_html'] = attachment.get("video_html", "")


@app.event("app_mention")
def handle_bot_mention(body, ack, event, say, logger):
    """Handle bot mention"""
    logger.info(body)
    ack()
    text = event.get("text", "")
    user = event.get("user", "")
    message = handle_event_text(text, user, say)
    if message:
        say(message)


@app.event("emoji_changed")
def handle_emoji_changed_events(event, ack, say, logger):
    """Handle emoji changed events"""
    logger.info(event)
    ack()
    name = event.get("name", "")
    subtype = event.get("subtype", "")
    if subtype == "add":
        say(
            channel=TRASH_CHANNEL_ID,
            text=f"Its not really my job, but you should know that an emoji has been added -> :{name}:"
        )


@app.event("team_join")
def ask_for_introduction(event, ack, say, logger):
    """When new user joins channel asks for introduction"""
    logger.info(event)
    ack()
    text = event.get("text", "")
    user = event.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    text = f"Welcome to the team, <@{user}>! 🎉 You can introduce yourself in this channel with a greeting trash video."
    say(channel=TRASH_CHANNEL_ID, text=text)


# <------------------------action------------------------------->
@app.action(re.compile("rate_video"))
def action_button_click(body, ack, say, logger):
    # Acknowledge the action
    ack()
    user = body.get("user", "")
    user_id = user.get("id", "")
    value = body['actions'][0]['value']
    video_id = value.split(" ")[0]
    rating = value.split(" ")[1]
    logger.info(f"User {user_id} rated video {video_id} with {rating}")
    if data_manager.user_already_rated(video_id, user_id)['exists']:
        logger.info(f"User {user_id} already rated video {video_id}")
        return
    data_manager.insert_rating(video_id, user_id, rating)


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
    ack()
    playlist = data_manager.get_all_videos()
    response = ""
    for video in playlist:
        response += f'#{video["id"]} -> https://www.youtube.com/watch?v={video["video_id"]}\n'
    respond(response)


@app.command("/add")
def handle_add_command(ack, body, respond, logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    ack()
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    response = save_video(text, user_id)
    respond(response)


@app.command("/send-to-channel")
def handle_private_video_send(client, ack, body, respond, logger):
    """Sends a random video to the channel with message and mentions"""
    logger.info(body)
    ack()
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    receiver = text.split("/")[0] if "/" in text else text
    message = text.split("/")[1] if "/" in text else None
    video_response = get_random_video()
    if not video_response:
        return respond(BOT.random_error_reply())
    if not message:
        reply_text = BOT.get_reply_text(receiver, user_id)
        text = reply_text+video_response
    else:
        reply_text = BOT.get_reply_text_with_message(receiver, user_id, message)
        text = reply_text+video_response
    client.chat_postMessage(channel=TRASH_CHANNEL_ID, text=text)


@app.command("/send-to-user")
def handle_private_video_send(client, ack, body, respond, logger):
    """Send a random video to a user with message and mentions"""
    ack()
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    receiver = text.split("/")[0] if "/" in text else text
    message = text.split("/")[1] if "/" in text else None
    recipient = receiver.split("|")[0][2:] if "|" in receiver else receiver
    dm_channel = client.conversations_open(users=recipient)
    logger.warning(dm_channel)
    if dm_channel:
        channel_id = dm_channel.get("channel", {}).get("id", "")
        video_response = get_random_video()
        if not video_response:
            return respond(BOT.random_error_reply())
        if not message:
            reply_text = BOT.get_reply_text(receiver, user_id)
            text = reply_text+video_response
        else:
            reply_text = BOT.get_reply_text_with_message(receiver, user_id, message)
            text = reply_text+video_response
        client.chat_postMessage(channel=channel_id, text=text)
        respond(BOT.random_success_reply())
    else:
        respond(BOT.random_error_reply())


# <------------------------shortcuts------------------------------->
@app.shortcut("save_shortcut")
def handle_shortcut_save(ack, body, respond, logger):
    """Save a video to the playlist"""
    logger.info(body)
    ack()
    message = body.get("message", "")
    text = message.get("text", "")
    user = body.get("user", "")
    user_id = user.get("id", "")
    response = save_video(text, user_id)
    respond(response)


# <------------------------error------------------------------->
@app.error
def custom_error_handler(error, body, logger):
    """Custom error handler"""
    logger.exception(f"Error: {error}")
    logger.info(f"Request body: {body}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

import os
import re

from dotenv import load_dotenv
from slack_bolt import *
from slack_bolt.adapter.socket_mode import SocketModeHandler

from src.bot import *
from src.bot.bot import TrashBot
import logging

from src.data_manager import data_manager
from src.utils import utils, blocks

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


def handle_event_text(text: str, user: str, say: Say) -> str:
    """Handle a bot commands"""
    if "help" in text.lower():
        return BOT.help()
    if any(word in text.lower() for word in TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS):
        return utils.get_random_video_response(say, BOT)
    if any(word in text.lower() for word in TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS):
        return save_video(text, user)
    if "good bot" in text.lower():
        return BOT.random_love_reply()
    if "bad bot" in text.lower():
        return BOT.random_hate_reply()
    if "source code" in text.lower():
        return 'https://github.com/NorbertRuff/trashBot'
    return TRASH_BOT_DONT_UNDERSTAND


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
        return BOT.general_error_reply()


# <------------------------message------------------------------->
@app.message("hello")
def handle_hello(message: dict, say: Say, ack: Ack, logger: logging.Logger):
    """Handle hello message"""
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.say_hi_to(user))


@app.message("good bot")
def handle_bot_love(message: dict, say: Say, ack: Ack, logger: logging.Logger):
    """Handle hello message"""
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.random_love_reply())


@app.message("bad bot")
def handle_bot_hate(message: dict, say: Say, ack: Ack, logger: logging.Logger):
    """Handle hello message"""
    logger.info(message)
    ack()
    user = message.get("user", "")
    if utils.user_is_bot(user, BOT_ID):
        return
    say(BOT.random_hate_reply())


# <------------------------events------------------------------->
@app.event("message")
def handle_message_events(message: dict, event: dict, say: Say, ack: Ack):
    """Handle message events"""
    ack()
    subtype = message.get("subtype", "")
    channel = message.get("channel", "")
    user = event.get("user", "")
    if not channel == TRASH_CHANNEL_ID:
        return
    if utils.user_is_bot(user, BOT_ID):
        return
    if not user:
        return
    if subtype == "channel_join":
        text = BOT.ask_for_introduction(user)
        say(channel=TRASH_CHANNEL_ID, text=text)


@app.event("app_mention")
def handle_bot_mention(body: dict, event: dict, say: Say, ack: Ack, logger: logging.Logger):
    """Handle bot mention"""
    logger.info(body)
    ack()
    text = event.get("text", "")
    user = event.get("user", "")
    message = handle_event_text(text, user, say)
    if message:
        say(message)


@app.event("emoji_changed")
def handle_emoji_changed_events(event: dict, say: Say, ack: Ack, logger: logging.Logger):
    """Handle emoji changed events"""
    logger.info(event)
    ack()
    emoji_name = event.get("name", "")
    subtype = event.get("subtype", "")
    if subtype == "add":
        say(
            channel=TRASH_CHANNEL_ID,
            text=BOT.get_emoji_event_response(emoji_name)
        )


@app.event("team_join")
def handle_team_join_events(event: dict, say: Say, ack: Ack, logger: logging.Logger):
    """Handle team join events"""
    logger.info(event)
    ack()
    user = event.get("user", "").get("id", "")
    channel = event.get("channel", "")
    if not user or not channel == TRASH_CHANNEL_ID:
        return
    if utils.user_is_bot(user, BOT_ID):
        return
    text = BOT.ask_for_introduction(user)
    say(channel=TRASH_CHANNEL_ID, text=text)


@app.event("app_home_opened")
def update_home_tab(event: dict, client, ack: Ack, logger: logging.Logger):
    logger.info(event)
    ack()
    user_id = event.get("user")
    try:
        client.views_publish(
            user_id=user_id,
            view=blocks.get_home_view_blocks(user_id)
        )
    except Exception as e:
        logger.error(f"Error publishing view to Home Tab: {e}")


# <------------------------action------------------------------->
@app.action(re.compile("rate_video"))
def action_button_click(body: dict, ack: Ack, logger: logging.Logger):
    # Acknowledge the action
    logger.info(body)
    ack()
    user_id = body.get("user", "").get("id", "")
    value = body['actions'][0]['value'] if 'actions' in body else None
    video_id = value.split(" ")[0]
    rating = value.split(" ")[1]
    logger.info(f"User {user_id} rated video {video_id} with {rating}")
    if data_manager.user_already_rated(video_id, user_id)['exists']:
        logger.info(f"User {user_id} already rated video {video_id}")
        return
    data_manager.insert_rating(video_id, user_id, rating)


# <------------------------modals------------------------------->
@app.action("open_send_trash_to_user_modal")
def handle_open_send_trash_to_user_modal(body: dict, client: App.client, ack: Ack, logger: logging.Logger):
    logger.info(body)
    ack()
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=blocks.get_send_trash_to_user_modal()
        )
    except Exception as e:
        logger.error(f"Error publishing view to Home Tab: {e}")


@app.action("open_send_trash_to_channel_modal")
def handle_open_send_trash_to_user_modal(body: dict, client: App.client, ack: Ack, logger: logging.Logger):
    logger.info(body)
    ack()
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=blocks.get_send_trash_to_channel_modal()
        )
    except Exception as e:
        logger.error(f"Error publishing view to Home Tab: {e}")


@app.view("send_user_trash_modal")
def handle_send_user_video_modal_submission(payload: dict, body: dict, client, ack: Ack, logger: logging.Logger):
    logger.info(body)
    ack()
    user_id = body.get("user", "").get("id", "")
    values = payload.get("state", "").get("values", "")
    message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
    selected_user = values.get("selected_user", "").get("selected_user", "").get("value", "")
    logger.info(f"User {user_id} sent message {message_to_send} to user {selected_user}")
    client.chat_postMessage(
        channel=TRASH_CHANNEL_ID,
        text=f"User {user_id} sent message {message_to_send} to user {selected_user}"
    )


@app.view("send_channel_trash_modal")
def handle_send_user_video_modal_submission(payload: dict, body: dict, client, ack: Ack, logger: logging.Logger):
    logger.info(body)
    ack()
    user_id = body.get("user", "").get("id", "")
    values = payload.get("state", "").get("values", "")
    message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
    client.chat_postMessage(
        channel=TRASH_CHANNEL_ID,
        text=f"User {user_id} sent message {message_to_send}"
    )


# <------------------------command------------------------------->
@app.command("/help")
def handle_help_command(body: dict, respond: Respond, ack: Ack, logger: logging.Logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    ack()
    respond(BOT.help())


@app.command("/list")
def handle_list_command(body: dict, respond: Respond, ack: Ack, logger: logging.Logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    ack()
    playlist = data_manager.get_all_videos()
    response = ""
    for video in playlist:
        response += f'#{video["id"]} -> https://www.youtube.com/watch?v={video["video_id"]}\n'
    respond(response)


@app.command("/add")
def handle_add_command(body: dict, respond: Respond, ack: Ack, logger: logging.Logger):
    """Responds with the bot usage helper message"""
    logger.info(body)
    ack()
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    response = save_video(text, user_id)
    respond(response)


@app.command("/send-to-channel")
def handle_private_video_send(body: dict, respond: Respond, client: App.client, ack: Ack, logger: logging.Logger):
    """Sends a random video to the channel with message and mentions"""
    logger.info(body)
    ack()
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    receiver = text.split("/")[0] if "/" in text else text
    message = text.split("/")[1] if "/" in text else None
    video = utils.get_random_video_from_db()
    video_response = BOT.get_reply_text_from_video_row(video)
    if not video_response:
        return respond(BOT.random_error_reply())
    if not message:
        reply_text = BOT.get_reply_text(receiver, user_id)
        text = reply_text + video_response
    else:
        reply_text = BOT.get_reply_text_with_message(receiver, user_id, message)
        text = reply_text + video_response
    client.chat_postMessage(channel=TRASH_CHANNEL_ID, text=text)


@app.command("/send-to-user")
def handle_private_video_send(body: dict, respond: Respond, client: App.client, ack: Ack, logger: logging.Logger):
    """Send a random video to a user with message and mentions"""
    logger.info(body)
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
        video = utils.get_random_video_from_db()
        video_response = BOT.get_reply_text_from_video_row(video)
        if not video_response:
            return respond(BOT.random_error_reply())
        if not message:
            reply_text = BOT.get_reply_text(receiver, user_id)
            text = reply_text + video_response
        else:
            reply_text = BOT.get_reply_text_with_message(receiver, user_id, message)
            text = reply_text + video_response
        client.chat_postMessage(channel=channel_id, text=text)
        respond(BOT.random_success_reply())
    else:
        respond(BOT.random_error_reply())


@app.command("/surprise")
def handle_surprise_command(body: dict, respond: Respond, say: Say, ack: Ack, logger: logging.Logger):
    """Send a random video to a user with message and mentions"""
    logger.info(body)
    ack()
    text = body.get("text", "")
    user_id = body.get("user_id", "")
    video = utils.get_random_video_from_db()
    video_response = BOT.get_reply_text_from_video_row(video)
    video_id = video.get("video_id", "")
    if not video_response:
        respond(BOT.random_error_reply())
    else:
        text = f"<@{user_id}> asked for a random video. {BOT.random_general_reply()} \n {video_response}"
    say(channel=TRASH_CHANNEL_ID, text=text)
    say(channel=TRASH_CHANNEL_ID, text=blocks.get_rating_section(video_id))


@app.command("/message-to-channel")
def handle_message_to_channel_command(body: dict, respond: Respond, say: Say, ack: Ack, logger: logging.Logger):
    """Sends a message to the channel"""
    logger.info(body)
    ack()
    text = body.get("text", "")
    if not text:
        respond(BOT.random_error_reply())
    else:
        text = text
    say(channel=TRASH_CHANNEL_ID, text=text)


# <------------------------shortcuts------------------------------->
@app.shortcut("save_shortcut")
def handle_shortcut_save(body: dict, respond: Respond, ack: Ack, logger: logging.Logger):
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
def custom_error_handler(error, body: dict, logger: logging.Logger):
    """Custom error handler"""
    logger.exception(f"Error: {error}")
    logger.info(f"Request body: {body}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

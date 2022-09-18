import logging
import logging
import os

from dotenv import load_dotenv
from slack_bolt import *
from slack_bolt.adapter.socket_mode import SocketModeHandler

from src.listeners import CommandListener, EventListener, MessageListener, ViewListener, ShortcutListener, \
    ActionListener
from src.slack_bot import TrashBot

load_dotenv()

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
TRASH_CHANNEL_ID = os.environ["TRASH_CHANNEL_ID"]
app = App(token=SLACK_BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

bot_id = app.client.auth_test()["user_id"]
bot_name = app.client.auth_test()["user"]

bot = TrashBot(bot_id, bot_name, TRASH_CHANNEL_ID)
logging.getLogger().warning(f"BOT_ID: {bot_id} -> BOT_NAME: {bot_name}")
logging.getLogger().warning(bot.bot_id)

command_listener = CommandListener(app, bot, TRASH_CHANNEL_ID)
message_listener = MessageListener(app, bot, TRASH_CHANNEL_ID)
event_listener = EventListener(app, bot, TRASH_CHANNEL_ID)
action_listener = ActionListener(app, bot, TRASH_CHANNEL_ID)
view_listener = ViewListener(app, bot, TRASH_CHANNEL_ID)
shortcuts_listener = ShortcutListener(app, bot, TRASH_CHANNEL_ID)


# <------------------------error------------------------------->
@app.error
def custom_error_handler(error, body: dict, logger: logging.Logger):
    """Custom error handler"""
    logger.exception(f"Error: {error}")
    logger.info(f"Request body: {body}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

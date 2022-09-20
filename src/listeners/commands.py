from logging import Logger

from slack_bolt import App, Respond, Ack, Say

from src import data_manager, utils
from src.slack_bot import TrashBot
from src.utils import save_video, blocks


# <------------------------command------------------------------->
class CommandListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app = bolt_app
        self.app.command("/help")(self.handle_help_command)
        self.app.command("/list")(self.handle_list_command)
        self.app.command("/add")(self.handle_add_command)
        self.app.command("/surprise")(self.handle_surprise_command)
        self.app.command("/message-to-channel")(self.handle_message_to_channel_command)

    def handle_help_command(self, body: dict, respond: Respond, ack: Ack, logger: Logger):
        """Responds with the slackBot usage helper message"""
        logger.info(body)
        ack()
        respond(self.bot.help())

    def handle_list_command(self, body: dict, respond: Respond, ack: Ack, logger: Logger):
        """Responds with the slackBot usage helper message"""
        logger.info(body)
        ack()
        playlist = data_manager.get_all_videos()
        response = ""
        for video in playlist:
            response += f'#{video["id"]} {video["title"]} -> https://www.youtube.com/watch?v={video["video_id"]}\n'
        respond(response)

    def handle_add_command(self, body: dict, respond: Respond, ack: Ack, logger: Logger):
        """Responds with the slackBot usage helper message"""
        logger.info(body)
        ack()
        text = body.get("text", "")
        user_id = body.get("user_id", "")
        response = save_video(text, user_id, self.bot)
        respond(response)

    def handle_surprise_command(self, body: dict, respond: Respond, say: Say, ack: Ack, logger: Logger):
        """Send a random video to a user with message and mentions"""
        logger.info(body)
        ack()
        text = body.get("text", "")
        user_id = body.get("user_id", "")
        video_db_row = utils.get_random_video_db_row()
        video_response = self.bot.get_reply_text_from_video_row(video_db_row)
        video_id = video_db_row.get("video_id", "")
        if not video_response:
            respond(self.bot.random_error_reply())
        else:
            text = f"<@{user_id}> asked for a random video. {self.bot.random_general_reply()} \n {video_response}"
        say(channel=self.trash_channel_id, text=text)
        say(channel=self.trash_channel_id, text=blocks.get_rating_section(video_id))

    def handle_message_to_channel_command(self, body: dict, respond: Respond, say: Say, ack: Ack,
                                          logger: Logger):
        """Sends a message to the channel"""
        logger.info(body)
        ack()
        text = body.get("text", "")
        if not text:
            respond(self.bot.random_error_reply())
        else:
            text = text
        say(channel=self.trash_channel_id, text=text)

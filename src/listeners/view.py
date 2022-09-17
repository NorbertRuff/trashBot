import logging

from slack_bolt import App, Ack

from src.slack_bot import TrashBot


# <------------------------views------------------------------->
class ViewListener:
    def __init__(self, bolt_app: App, bot: TrashBot, trash_channel_id: str):
        self.app = bolt_app
        self.bot = bot
        self.trash_channel_id = trash_channel_id
        self.app.view("send_user_trash_modal")(self.handle_modal_submission_trash_to_user)
        self.app.view("send_channel_trash_modal")(self.handle_modal_submission_trash_to_channel)

    def handle_modal_submission_trash_to_user(self, payload: dict, body: dict, client, ack: Ack,
                                              logger: logging.Logger):
        logger.info(body)
        ack()
        user_id = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
        selected_user = values.get("selected_user", "").get("selected_user", "").get("value", "")
        logger.info(f"User {user_id} sent message {message_to_send} to user {selected_user}")
        client.chat_postMessage(
            channel=self.trash_channel_id,
            text=f"User {user_id} sent message {message_to_send} to user {selected_user}"
        )

    def handle_modal_submission_trash_to_channel(self, payload: dict, body: dict, client, ack: Ack,
                                                 logger: logging.Logger):
        logger.info(body)
        ack()
        user_id = body.get("user", "").get("id", "")
        values = payload.get("state", "").get("values", "")
        message_to_send = values.get("message_to_send", "").get("message_to_send", "").get("value", "")
        client.chat_postMessage(
            channel=self.trash_channel_id,
            text=f"User {user_id} sent message {message_to_send}"
        )

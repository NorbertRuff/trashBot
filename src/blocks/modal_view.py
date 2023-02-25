from blockkit import Input, UsersSelect, PlainTextInput, Modal, \
    Section, ImageBlock, Divider, Home, StaticSelect, PlainOption

from src.blocks import get_forward_and_back_navigate_button, get_home_button, get_divider_block, get_image_section, \
    get_image_actions


def get_send_trash_to_user_modal(video_id=None) -> dict:
    """Builds and returns the send trash to user modal"""
    if video_id:
        return Modal(
            title="TrashBot",
            submit="Send",
            close="Cancel",
            callback_id=f"send_user_trash_modal",
            blocks=[
                Section(text="*Send a trash video to a user in a DM*"),
                ImageBlock(
                    image_url=f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
                    alt_text=f"{video_id}"),
                Input(
                    element=UsersSelect(placeholder="Select a user", action_id="selected_user"),
                    label="User", optional=False, block_id="selected_user"
                ),
                Input(
                    element=PlainTextInput(action_id="message_to_send"),
                    label="Message", optional=True, block_id="message_to_send"
                ),
            ],
        ).build()
    return Modal(
        title="TrashBot",
        submit="Send",
        close="Cancel",
        callback_id="send_user_trash_modal",
        blocks=[
            Section(text="*Send someone a random trash video*"),
            Input(
                element=PlainTextInput(action_id="message_to_send"),
                label="Message", optional=True, block_id="message_to_send"
            ),
            Input(
                element=UsersSelect(placeholder="Select a user", action_id="selected_user"),
                label="Select a user", block_id="selected_user", optional=False
            ),
        ],
    ).build()


def get_send_trash_to_channel_modal() -> dict:
    """Builds and returns the send trash to channel modal"""
    payload = Modal(
        title="TrashBot",
        submit="Send",
        close="Cancel",
        callback_id="send_channel_trash_modal",
        blocks=[
            Section(text="*Send a random trash video to the trash channel*"),
            Input(
                element=PlainTextInput(action_id="message_to_send"),
                label="Message", optional=True, block_id="message_to_send"
            ),
        ],
    ).build()
    return payload


def get_send_challenge_to_channel_modal() -> dict:
    """Builds and returns the send challenge to channel modal"""
    payload = Modal(
        title="TrashBot",
        submit="Send",
        close="Cancel",
        callback_id="send_channel_challenge_modal",
        blocks=[
            Section(text="*Are you sure you want to send a challenge to the trash channel*"),
        ],
    ).build()
    return payload


def get_save_challenge_to_db_modal() -> dict:
    """Builds and returns the save challenge to db modal"""
    payload = Modal(
        title="TrashBot",
        submit="Save",
        close="Cancel",
        callback_id="save_challenge_modal",
        blocks=[
            Section(text="*Save a challenge to the trash db*"),
            Section(
                text="Pick a challenge type",
                block_id="challenge_type",
                accessory=StaticSelect(
                    placeholder="Select an item",
                    options=[
                        PlainOption(text="Picture", value="picture"),
                        PlainOption(text="Text", value="text"),
                    ],
                    action_id="static_select_type",
                    initial_option=PlainOption(text="Picture", value="picture"),
                ),
            ),
            Section(
                text="Pick a category",
                block_id="challenge_category",
                accessory=StaticSelect(
                    placeholder="Select an item",
                    options=[
                        PlainOption(text="Blast from the past", value="BLAST_FROM_THE_PAST"),
                        PlainOption(text="The best of the best", value="THE_BEST_OF_THE_BEST"),
                        PlainOption(text="The worst of the worst", value="THE_WORST_OF_THE_WORST"),
                        PlainOption(text="Get to know each other", value="GET_TO_KNOW_EACH_OTHER"),
                        PlainOption(text="Pure fantasy", value="PURE_FANTASY"),
                        PlainOption(text="Weird and wonderful", value="WEIRD_AND_WONDERFUL"),
                        PlainOption(text="History lesson", value="HISTORY_LESSON"),
                        PlainOption(text="Hidden talent", value="HIDDEN_TALENT"),
                        PlainOption(text="Hidden treasure", value="HIDDEN_TREASURE"),
                        PlainOption(text="First date questions", value="FIRST_DATE_QUESTIONS"),
                        PlainOption(text="Undefinable", value="UNDEFINABLE"),
                    ],
                    action_id="static_select_category",
                    initial_option=PlainOption(text="Blast from the past", value="BLAST_FROM_THE_PAST"),
                ),
            ),
            Input(
                element=PlainTextInput(action_id="challenge_text"),
                label="Challenge text", optional=False, block_id="challenge_text"
            ),
        ],
    ).build()
    return payload


def get_save_trash_modal() -> dict:
    """Builds and returns the send trash to channel modal"""
    payload = Modal(
        title="TrashBot",
        submit="Save",
        close="Cancel",
        callback_id="save_trash_modal",
        blocks=[
            Section(text="*Save a trash video*"),
            Input(
                element=PlainTextInput(action_id="youtube_url"),
                label="Youtube Url", optional=False, block_id="youtube_url"
            ),
        ],
    ).build()
    return payload


def get_video_list_modal(videos: list, offset: int) -> dict:
    """Builds and returns the video list modal"""
    video_blocks = []
    videos_length = len(videos)
    limit = 10
    video_blocks.append(get_home_button())
    for i in range(offset, offset + limit):
        if i >= videos_length:
            break
        video_blocks.append(get_image_section(videos[i]))
        video_blocks.append(get_image_actions(videos[i]))
        video_blocks.append(get_divider_block())
    video_blocks.append(
        get_forward_and_back_navigate_button(backward_offset=offset - limit, forward_offset=offset + limit,
                                             videos_length=videos_length))
    payload = Home(
        blocks=[Divider()],
    ).build()
    payload["blocks"].extend(video_blocks)
    return payload

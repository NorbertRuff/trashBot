"""
Blocks for the home tab, messages and modals
"""

from blockkit import Button, Divider, Header, Home, Input, Message, UsersSelect, PlainTextInput, Modal, \
    Actions, ConversationsSelect, Image, enums, Section, ImageBlock


def get_rating_section(video_id: str) -> dict:
    """Builds and returns the rating section interactive block section for a video"""
    rate_block = Message(
        text="Rate this video!",
        blocks=[
            Section(text="Rate this video!"),
            Actions(
                elements=[
                    Button(text="1", style=enums.Style.danger, value=f"{video_id} 1", action_id="rate_video_1"),
                    Button(text="2", value=f"{video_id} 2", action_id="rate_video_2"),
                    Button(text="3", value=f"{video_id} 3", action_id="rate_video_3"),
                    Button(text="4", value=f"{video_id} 4", action_id="rate_video_4"),
                    Button(text="5", style=enums.Style.primary, value=f"{video_id} 5", action_id="rate_video_5"),
                ]
            ),
        ]
    ).build()
    return rate_block


def get_help_block() -> dict:
    """Builds and returns the help block"""
    return Home(
        blocks=[
            Actions(elements=[Button(text="Back to the home screen", value="home", action_id="home_button")]),
            Header(text="--|Help|-- :question:"),
            Section(
                text="*Shortcut for saving*. \n Message shortcuts are available in the More actions menu from any message."),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/shortcut_ex2.png",
                alt_text="shortcut_ex2",
            ),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/shortcut_ex1.png",
                alt_text="shortcut_ex1",
            ),
            Divider(),
            Section(
                text="*Commands*.\n Slash commands allow you to complete an action with an app simply by sending a message in Slack."
                     " Type double forward slash (//) in the message to view a list of available slash commands. /help and /list are only visible for you."),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/commands_ex.png",
                alt_text="commands_ex",
            ),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/commands.png",
                alt_text="commands_ex",
            ),
            Divider(),
            Section(
                text="*Message inline commands*.\n Type a @ in any message and provide keywords that TrashBot understands."),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/random.png",
                alt_text="random_trash",
            ),
            ImageBlock(
                title="Ask for a random trash video",
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/surprise.png",
                alt_text="surprise",
            ),
            Divider(),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/add.png",
                alt_text="add",
            ),
            ImageBlock(
                title="Save a video to the database",
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/save.png",
                alt_text="save",
            ),
            Divider(),
            ImageBlock(
                title="Prints the help message to the channel",
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/help.png",
                alt_text="help",
            ),
            Divider(),
            ImageBlock(
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/bad_bot.png",
                alt_text="bad_bot",
            ),
            ImageBlock(
                title="Pet the bot",
                image_url="https://raw.githubusercontent.com/NorbertRuff/trashBot/master/blob/good_bot.png",
                alt_text="good_bot",
            ),
            Divider()
        ]).build()


def get_home_view_blocks(user_id) -> dict:
    """Builds and returns the home view blocks"""
    payload = Home(
        blocks=[
            Header(text="Welcome to the TrashBot User Interface (TUI)!"),
            Section(text=f"Hi there <@{user_id}> :wave:, how can I help you today?"),
            Header(text="--|Help|-- :question:"),
            Section(
                text="*Navigates you to the help page*",
                accessory=Button(
                    text=":sos:", value="help", action_id="open_help_page"
                ),
            ),
            Header(text="--|Actions|-- :robot_face:"),
            Section(
                text="*Send a random trash video for a user in a direct message*\nyou can also provide a message for it",
                accessory=Button(
                    text=":incoming_envelope: ", value="send_trash_to_user", action_id="open_send_trash_to_user_modal"
                ),
            ),
            Divider(),
            Section(
                text="*Send a random trash video for the trash channel*\nyou can also provide a message for it",
                accessory=Button(
                    text=":movie_camera:", value="send_trash_to_channel", action_id="open_send_trash_to_channel_modal"
                ),
            ),
            Divider(),
            Section(
                text="*Check all the trash videos saved in the database*",
                accessory=Button(
                    text=":put_litter_in_its_place:", value="list_trash_videos",
                    action_id="open_list_trash_videos_modal"
                ),
            ),
            Divider(),
            Section(
                text="*Save a video to the trash database*",
                accessory=Button(
                    text=":floppy_disk:", value="add_trash_video", action_id="open_add_trash_videos_modal"
                ),
            ),
            Divider(),
            Section(
                text="My source code is here :point_right: <https://github.com/NorbertRuff/trashBot|TrashBot on github>"
            ),
            Section(
                text="Feel free to contribute :wink:, request features :bulb: or report bugs :bug:"
            ),
        ]
    ).build()
    return payload


def get_conversation_select_block() -> dict:
    """Builds and returns the conversation select block"""
    payload = Message(
        text="Please select a conversation",
        blocks=[
            Section(text="Please select a conversation"),
            Actions(
                elements=[
                    ConversationsSelect(placeholder="Select a conversation", action_id="actionId-1"),
                    Button(text="Send", value="click_me_123", action_id="button-action"),
                ]
            ),
        ]
    ).build()
    return payload


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


def get_video_block_from_yt_details(video_details: dict) -> dict:
    """Builds and returns the video block from the YouTube video details"""
    video_block = {
        "type": "video",
        "title": {
            "type": "plain_text",
            "text": f"{video_details['title']}",
            "emoji": True
        },
        "title_url": f"https://www.youtube.com/watch?v={video_details['video_id']}",
        "video_url": f"https://www.youtube.com/embed/{video_details['video_id']}?feature=oembed&autoplay=1",
        "alt_text": f"{video_details['fallback']}",
        "thumbnail_url": f"https://i.ytimg.com/vi/{video_details['video_id']}/hqdefault.jpg",
        "author_name": f"{video_details['author_name']}",
        "provider_name": "YouTube",
        "provider_icon_url": "https://a.slack-edge.com/80588/img/unfurl_icons/youtube.png"
    }
    return video_block


def get_back_navigate_button(offset: int):
    """Builds and returns the back navigate button"""
    return Button(text="Previous page", action_id="navigate backward", value=f"{offset}")


def get_forward_navigate_button(offset: int):
    """Builds and returns the forward navigate button"""
    return Button(text="Next page", action_id="navigate forward", value=f"{offset}")


def get_forward_and_back_navigate_button(backward_offset: int, forward_offset: int, videos_length: int) -> dict:
    """Builds and returns the front and back navigate block"""
    elements = []
    if backward_offset < 0:
        elements.append(get_forward_navigate_button(forward_offset))
        return Actions(elements=elements).build()
    if forward_offset >= videos_length:
        elements.append(get_back_navigate_button(backward_offset))
        return Actions(elements=elements).build()
    elements.append(get_back_navigate_button(backward_offset))
    elements.append(get_forward_navigate_button(forward_offset))
    return Actions(elements=elements).build()


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


def get_divider_block() -> dict:
    """Builds and returns the divider block"""
    return Divider().build()


def get_home_button() -> dict:
    """Builds and returns the home button"""
    return Actions(elements=[Button(text="Back to the home screen", value="home", action_id="home_button")]).build()


def get_image_section(video_db_row: dict) -> dict:
    """Builds and returns the image section block"""
    return Section(
        text=f"#*{video_db_row['id']}* -> "
             f"*{video_db_row['title']}*"
             f"\n {video_db_row['author_name']} "
             f"\n https://www.youtube.com/watch?v={video_db_row['video_id']}",
        accessory=Image(
            image_url=f"https://i.ytimg.com/vi/{video_db_row['video_id']}/hqdefault.jpg",
            alt_text=f"{video_db_row['fallback']}",
        ),
    ).build()


def get_image_actions(video_db_row: dict) -> dict:
    """Builds and returns the image actions block"""
    return Actions(
        elements=[
            Button(
                text="Send to channel",
                value=f"send_to_channel {video_db_row['id']}",
                action_id=f"send_to_channel_button_action",
            ),
            Button(
                text="Send to a user",
                value=f"{video_db_row['video_id']}",
                action_id=f"send_to_user_from_list_button_action",
            ),
        ]
    ).build()


def get_send_to_channel_block(video_id: str) -> dict:
    """Builds and returns the send to channel button block"""
    block = Section(
        text="Send this :point_up: to the trash channel.",
        accessory=Button(
            text="Send", value=f"send_to_channel {video_id}", action_id="send_to_channel_button_action"
        ),
    ).build()
    return block

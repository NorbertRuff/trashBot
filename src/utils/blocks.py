from blockkit import (
    Actions,
    Button,
    ConversationsSelect,
    Divider,
    Message,
    Section,
    Modal,
    UsersSelect,
    Home,
    PlainTextInput,
    Input,
    Header,
    enums,
)


def get_rating_section(video_id: str) -> dict:
    """Get the rating section interactive block section for a video"""
    rate_block = Message(
        text="How painful is this video? Rate it!",
        blocks=[
            Section(text="How painful is this video? Rate it!"),
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


def get_home_view_blocks(user_id):
    payload = Home(
        blocks=[
            Header(text="TrashUI!"),
            Section(text=f"Hi there <@{user_id}> :wave:, how can I help you today?\n\n *Select an action:*"),
            Divider(),
            Section(
                text="Send a random trash video for a user in a DM",
                accessory=Button(
                    text="Use", value="end_trash_to_user", action_id="open_send_trash_to_user_modal"
                ),
            ),
            Divider(),
            Section(
                text="Send a random trash video for the trash channel",
                accessory=Button(
                    text="Use", value="send_trash_to_channel", action_id="open_send_trash_to_channel_modal"
                ),
            ),
            Divider(),
            Section(
                text="Check all the trash videos saved in the database",
                accessory=Button(
                    text="Use", value="list_trash_videos", action_id="open_list_trash_videos_modal"
                ),
            ),
        ]
    ).build()
    return payload


def get_conversation_select_block():
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


def get_send_trash_to_user_modal():
    payload = Modal(
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
    return payload


def get_send_trash_to_channel_modal():
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


def get_video_block_from_yt_details(video_details: dict) -> dict:
    """Get the video block from the YouTube video details"""
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


def get_video_list_modal(videos: list, offset: int) -> dict:
    """Get the video list modal"""
    video_blocks = []
    limit = 10
    for i in range(offset, offset + limit):
        video_blocks.append(get_video_block_from_yt_details(videos[i]))
        video_blocks.append(get_send_to_channel_block(videos[i]["id"]))
        video_blocks.append(get_divider_block())
    payload = Home(
        blocks=[Divider()],
    ).build()
    payload["blocks"].extend(video_blocks)
    return payload


def get_divider_block():
    return Divider().build()


def get_send_to_channel_block(video_id: str) -> dict:
    """Get send to channel button block"""
    return Section(
        text="Send this :point_up: to the trash channel.",
        accessory=Button(
            text="Send", value=f"send_to_channel {video_id}", action_id="send_to_channel_button_action"
        ),
    ).build()

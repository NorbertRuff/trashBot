"""
Blocks for the home tab, messages and modals
"""

from blockkit import Button, Divider, Header, Home, Message, Actions, ConversationsSelect, Image, enums, Section


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


def get_image_section(video_db_row: dict) -> dict:
    """Builds and returns the image section block"""
    return Section(
        text=f"#*{video_db_row['id']}* -> "
             f"*{video_db_row['title']}*"
             f"\n\n*Garbage collected by: <@{video_db_row['user_id']}> *"
             f"\n\n {video_db_row['author_name']} "
             f"\n\n https://www.youtube.com/watch?v={video_db_row['video_id']}",
        accessory=Image(
            image_url=f"https://i.ytimg.com/vi/{video_db_row['video_id']}/hqdefault.jpg",
            alt_text=f"{video_db_row['fallback']}",
        ),
    ).build()


def get_top_users_section(users: list) -> dict:
    """Builds and returns the top garbage collectors block"""
    payload = Home(
        blocks=[
            Actions(elements=[Button(text="Back to the home screen", value="home", action_id="home_button")]),
            Header(text="--|Top Garbage collectors|-- :trophy:"), ]
    ).build()
    payload["blocks"].append(Divider().build())
    for i in range(len(users)):
        if i == 0:
            payload["blocks"].append(
                Section(
                    text=f"{i + 1}. :first_place_medal: <@{users[i]['user_id']}> -> {users[i]['video_count']} videos").build())
        elif i == 1:
            payload["blocks"].append(Section(
                text=f"{i + 1}. :second_place_medal: <@{users[i]['user_id']}> -> {users[i]['video_count']} videos").build())
        elif i == 2:
            payload["blocks"].append(
                Section(
                    text=f"{i + 1}. :third_place_medal: <@{users[i]['user_id']}> -> {users[i]['video_count']} videos").build())
        else:
            payload["blocks"].append(
                Section(text=f"{i + 1}. <@{users[i]['user_id']}> -> {users[i]['video_count']} videos").build())
    payload["blocks"].append(Divider().build())
    return payload


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

from blockkit import Button, Divider, Header, Home, Section


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
                text="*Check top 10 garbage collectors*",
                accessory=Button(
                    text=":trophy:", value="top_users", action_id="open_top_users_modal"
                ),
            ),
            Divider(),
            Section(
                text="*Send a random challenge to channel*",
                accessory=Button(
                    text=":thought_balloon:", value="challenge", action_id="open_send_challenge_to_channel_modal"
                ),
            ),
            Divider(),
            Section(
                text="*Save a new challenge to trash database*",
                accessory=Button(
                    text=":ring_buoy:", value="save_challenge", action_id="open_save_challenge_to_db_modal"
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

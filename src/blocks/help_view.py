from blockkit import Button, Divider, Header, Home, Actions, Section, ImageBlock


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

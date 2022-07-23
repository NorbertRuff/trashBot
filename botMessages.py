import os

from dotenv import load_dotenv

load_dotenv()
PLAYLIST_ID = os.environ["PLAYLIST_ID"]

TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

Mention me in a message and I can do the following: 
    @trashbot help -> Print this message
    @trashbot random trash -> I will get a random trash for you
    @trashbot :point_up: save -> I will save the video from the previous post to the trash playlist
    @trashbot :point_right: save videoUrl ->  I will save the video in this message to the trash playlist

The trash playlist is here:
    https://www.youtube.com/playlist?list={PLAYLIST_ID}

You can check out my source code here:
    https://github.com/NorbertRuff/trashBot
"""

MESSAGE_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    },
}

# TRASHBOT_ID = os.environ.get('BOT_ID')
# TRASHBOT_AT = "<@" + TRASHBOT_ID + ">"
TRASH_BOT_REPLIES = ['This is a classic :point_right: ', 'Biip-bop-bup :robot_face: ', 'Voila!', 'I love trash :heart_eyes: ']
TRASH_BOT_SUCCESS_REPLIES = ['Success!! ', 'Biip-bop-bup :robot_face: ', 'Voila! It\'s done :robot_face: ']
TRASH_BOT_LOVE = 'WOW thanks :heart_eyes: I Love you'
TRASH_BOT_HATE = ':cry: sorry, I hate you'
TRASH_BOT_DONT_UNDERSTAND = 'Huh? I did not understand that'
TRASH_BOT_NOT_FOUND_LINK = 'I could not find a link in the message.'
TRASH_BOT_NOT_PREVIOUS_LINK = 'I could not find a link in the previous message. Please use the `save` command with :point_right:.'
TRASH_BOT_SHIT_HIT_THE_FAN = 'Something went wrong, shit hit the fan'


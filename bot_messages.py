import os

from dotenv import load_dotenv

load_dotenv()
PLAYLIST_ID = os.environ["PLAYLIST_ID"]

TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

Mention me in a message and I can do the following: 
    @trashbot + 'help' ->
     I will print this message
    @trashbot + 'playlist' ->
     I will give you the link to the trash playlist
    @trashbot + 'last' ->
     I will give you the link to the last captured video
    @trashbot + 'random' or 'surprise' or 'trash' or 'trash video' ->
     I will get a random trash for you
    @trashbot + :point_up: or :point_up_2: + 'save' or 'playlist' keyword ->
     I will save the video from the previous valid youtube link to the trash playlist
    @trashbot + :point_right: + 'save' or 'add' or 'add to trash' + <video Url> ->
      I will save the <video Url> in this message to the trash playlist

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


TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS = ['random', 'get', 'surprise', 'get a random', 'trash', 'trash video', 'random video']
TRASH_BOT_UPLOAD_LAST_VALID_URL_KEYWORDS = ['save', 'playlist']
TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS = ['save', 'add', 'add to playlist', 'add to trash']

TRASH_BOT_GENERAL_REPLIES = [':rocket: :boom: :point_right: ', 'Biip-bop-bup :robot_face: ', 'Voila!', 'I love trash :heart_eyes: ']
TRASH_BOT_SUCCESS_REPLIES = ['Success!! ', 'Biip-bop-bup :robot_face: ', 'Voila! It\'s done :robot_face: ']
TRASH_BOT_ERROR_REPLIES = ['Error! ', 'Biip-bop-bup :robot_face: ',  'I can\'t do that :robot_face: ']

TRASH_BOT_LOVE = 'WOW thanks :heart_eyes: I Love you'
TRASH_BOT_HATE = ':cry: sorry, I hate you'

TRASH_BOT_VIDEO_ADDED = ':white_check_mark: Video added to trash playlist'
TRASH_BOT_PLAYLIST = f'The trash playlist is here:\n https://www.youtube.com/playlist?list={PLAYLIST_ID}'
TRASH_BOT_DONT_UNDERSTAND = 'Huh? I did not understand that'
TRASH_BOT_NOT_FOUND_LINK = 'I could not find a link in this or in the previous message. Please use the command with :point_right: save <url>.'
TRASH_BOT_ALREADY_IN_PLAYLIST = ':robot_face: I already have this video in the trash playlist.'
TRASH_BOT_SHIT_HIT_THE_FAN = 'Something went wrong, shit hit the fan'


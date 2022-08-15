TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

I have some command shortcuts:
    /help - show this message
    /add - add a new trash video
    /surprise - I will get a random trash video for you
    /list - list all trash videos
    /delete - delete a trash video by id **IN PROGRESS**
    /rate - rate a trash video by id **IN PROGRESS**

I can also save a video with the shortcut you find when clicking on a message ... thingy.

Mention me in a message and I can do the following: 
    @trashBot + 'help' ->
     I will print this message
    @trashBot + 'list' ->
     I will list all of the videos from the trash playlist
    @trashBot + 'random' or 'surprise' or 'trash' or 'video' ->
     I will get a random trash for you
    @trashBot + :point_up: or :point_up_2: + 'save' or 'playlist' keyword ->
     I will save the video from the previous valid youtube link to the trash playlist
    @trashBot + :point_right: + 'save' or 'add' or 'add to trash' + <video Url> ->
      I will save the <video Url> in this message to the trash playlist

You can check out my source code here:
    https://github.com/NorbertRuff/trashBot

Also, feel free to join the trash bot development by contributing to the repository
"""

TRASH_BOT_GET_RANDOM_VIDEO_KEYWORDS = ['random', 'get', 'surprise', 'get a random', 'trash', 'trash video',
                                       'video']
TRASH_BOT_UPLOAD_THIS_VIDEO_KEYWORDS = ['save', 'add', 'add to playlist', 'add to trash']

TRASH_BOT_GENERAL_REPLIES = [':rocket: :boom: :point_right: ', 'Biip-bop-bup :robot_face: ', 'Voila!',
                             'I love trash :heart_eyes: ']
TRASH_BOT_SUCCESS_REPLIES = ['Success!! ', 'Biip-bop-bup :robot_face: ', 'Voila! It\'s done :robot_face: ']
TRASH_BOT_ERROR_REPLIES = ['Error! ', 'Biip-bop-bup uh oh :robot_face: ', 'I can\'t do that :robot_face: ']

TRASH_BOT_LOVE = ['WOW thanks :heart_eyes: I Love you', ':heart_eyes: :heart_eyes: :heart_eyes:']
TRASH_BOT_HATE = [':cry: sorry, I hate you', ':cry: Than fix me :robot-face:', ':cry: I hate you :cry:']

TRASH_BOT_VIDEO_ADDED = ':white_check_mark: Video added to trash playlist'
TRASH_BOT_DONT_UNDERSTAND = 'Huh? I did not understand that'
TRASH_BOT_NOT_FOUND_LINK = 'I could not find a link in this or in the previous message. Please use the command with :point_right: save <url>.'
TRASH_BOT_ALREADY_IN_PLAYLIST = ':robot_face: I already have this video in the trash playlist.'
TRASH_BOT_SHIT_HIT_THE_FAN = 'Something went wrong, shit hit the fan'

TRASH_BOT_RATE = {
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "How painful is this video? Rate it!"
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "1"
                    },
                    "style": "danger",
                    "value": "1"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "2"
                    },
                    "value": "2"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "3"
                    },
                    "value": "3"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "4"
                    },
                    "value": "4"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "5"
                    },
                    "style": "primary",
                    "value": "5"
                }
            ]
        }
    ]
}

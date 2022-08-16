TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

I have some command shortcuts:
    /help - show this message
    /add - add a new trash video
    /surprise - I will get a random trash video for you **IN PROGRESS**
    /list - list all trash videos
    /delete - delete a trash video by id **IN PROGRESS**
    /rate - rate a trash video by id **IN PROGRESS**

I can also save a video with the shortcut you find when clicking on a message ... thingy (meatballs menu?) and selecting the save shortcut.

Mention me in a message and I can do the following: 
    @trashBot + 'help' ->
     I will print this message
    @trashBot + 'list' ->
     I will list all of the videos from the trash playlist
    @trashBot + 'random' or 'surprise' or 'trash' or 'video' ->
     I will get a random trash for you
    @trashBot + 'save' or 'add' or 'add to trash' + <video Url> ->
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
TRASH_BOT_SUCCESS_REPLIES = ['Success!! ', 'Biip-bop-bup :robot_face: ', 'Voila! It\'s done :robot_face: ',
                             ':ok_hand: ', 'done! ', 'Wooohoo! ', ':thumbsup: ']
TRASH_BOT_ERROR_REPLIES = ['Error! ', 'Biip-bop-bup uh oh :robot_face: ', 'I can\'t do that :robot_face: ',
                           ':no_entry: ', ':no_entry_sign: ', ':no_good: ', 'shame :no_good: ']

TRASH_BOT_LOVE = ['WOW thanks :heart_eyes: I Love you', ':heart_eyes: :heart_eyes: :heart_eyes:',
                  'finally :heart_eyes:', 'you are the best :heart_eyes:']
TRASH_BOT_HATE = [':cry: sorry, I hate you', ':cry: Than fix me :robot-face:', ':cry: I hate you :cry:',
                  'Fix me very badly :cry:', 'I hate you too :heart_eyes:',
                  'you can fix me here: https://github.com/NorbertRuff/trashBot']

TRASH_BOT_VIDEO_ADDED = ':white_check_mark: Video added to trash playlist'
TRASH_BOT_DONT_UNDERSTAND = 'Huh? I did not understand that'
TRASH_BOT_NOT_FOUND_LINK = 'I could not find a link in this or in the previous message. Please use the command with /add <url>.'
TRASH_BOT_ALREADY_IN_PLAYLIST = ':robot_face: I already have this video in the trash playlist.'
TRASH_BOT_SHIT_HIT_THE_FAN = 'Something went wrong, shit hit the fan'
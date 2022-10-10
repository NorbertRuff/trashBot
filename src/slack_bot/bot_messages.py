"""
Message templates for the Slack bot.
"""

TRASHBOT_HELP_MSG = f"""
:rocket: Heeellloo I am TrashBot! I will manage this channels trash videos!

I have some command shortcuts press // in the message box to see them.:
    /help - show this message
    /add <youtube link> - add a new trash video
    /surprise - I will get a random trash video for you
    /list - list all trash videos

I can also save a video with the shortcut you will find when clicking on a message ... thingy (meatballs menu?) and selecting the save shortcut.

Also You can mention me in a message and I can do the following: 
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
                  'finally someone who loves trash :heart_eyes:', 'everyone loves me :heart_eyes:',
                  ':heart_eyes:', 'you are the best :heart_eyes:']
TRASH_BOT_HATE = [':cry: I\'m sorry, I hate you', ':cry: Well then fix me :robot_face: ', ':cry: I hate you :cry:',
                  'Fix me very badly :cry:', 'I hate you too :heart_eyes:',
                  'You can fix me here: https://github.com/NorbertRuff/trashBot']

TRASH_BOT_MESSAGE = ['add', 'add to playlist', 'add to trash']
TRASH_BOT_VIDEO_ADDED = ':white_check_mark: Video added to trash playlist'
TRASH_BOT_DONT_UNDERSTAND = ['Huh? I did not understand that', 'I don\'t understand that', 'I don\'t get it',
                             'What?', 'What do you mean?', 'I don\'t know what you mean',
                             ':thinking_face: :thinking_face: :thinking_face:',
                             ':question: :question: :question:', 'I don\'t know what you are saying',
                             'I don\'t know what you are trying to say']
TRASH_BOT_NOT_FOUND_LINK = 'I could not find a link in this or in the previous message. Please use the command with /add <url>.'
TRASH_BOT_ALREADY_IN_PLAYLIST = ':robot_face: I already have this video in the trash playlist.'
TRASH_BOT_SHIT_HIT_THE_FAN = 'Something went wrong, shit hit the fan'
TRASH_BOT_EMOJI_REPLIES = ['Its not really my job, but you should know that an emoji has been added',
                           'Great, an emoji has been added I\'m not sure if I should be happy or sad about this',
                           'Great news!, an emoji has been added', 'A new emoji has been added',
                           'I\'m not sure if I should be happy or sad about this',
                           'HYPER IMPORTANT NEWS: an emoji has been added',
                           'Something has been added, but I\'m not sure what it is',
                           'Keep calm and add an emoji',
                           'JOHN CENA HAS ADDED AN EMOJI, oh wait, it was someone else',
                           'I\'m doing my best, but I\'m not sure if I can handle this',
                           'My job is to add trash videos, but I also have to notify you that an emoji has been added',
                           'For some reason I have to tell you that an emoji has been added']

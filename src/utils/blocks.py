def get_rating_section(video_id: str) -> dict:
    """Get the rating section interactive block section for a video"""
    rate_block = {
        "text": "How painful is this video? Rate it from 1 to 5",
        "blocks": [
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
                        "value": f"{video_id} 1",
                        "action_id": "rate_video_1",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "2"
                        },
                        "value": f"{video_id} 2",
                        "action_id": "rate_video_2",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "3"
                        },
                        "value": f"{video_id} 3",
                        "action_id": "rate_video_3",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "4"
                        },
                        "value": f"{video_id} 4",
                        "action_id": "rate_video_4",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "5"
                        },
                        "style": "primary",
                        "value": f"{video_id} 5",
                        "action_id": "rate_video_5",
                    }
                ]
            }
        ]
    }
    return rate_block


def get_home_view_blocks(user_id):
    return [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Hi there <@{user_id}> :wave:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Welcome to your _App's Home_ :tada:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            "Learn how home tabs can be more useful and interactive "
                            "<https://api.slack.com/surfaces/tabs/using|*in the documentation*>."
                        )
                    }
                }
            ]

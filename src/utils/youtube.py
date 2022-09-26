"""
Fetches the video metadata from YouTube
"""

import json
import urllib
import urllib.request


def get_youtube_video_info(video_id):
    """Fetches the video metadata from YouTube"""
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_id}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
    return data

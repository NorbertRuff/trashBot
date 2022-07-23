import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pickle

PLAYLIST_ID = os.environ["PLAYLIST_ID"]
scopes = [os.environ["SCOPE"]]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
YOUTUBE_CLIENT_SECRETS_FILE = "client_secret.json"


def get_authenticated_service():
    """Returns an instance of an Authenticated YouTube service object."""
    if os.path.exists("CREDENTIALS_PICKLE_FILE"):
        with open("CREDENTIALS_PICKLE_FILE", 'rb') as f:
            credentials = pickle.load(f)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            YOUTUBE_CLIENT_SECRETS_FILE, scopes)
        credentials = flow.run_local_server()
    youtube_service = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)
    with open("CREDENTIALS_PICKLE_FILE", 'wb') as f:
        pickle.dump(credentials, f)
    return youtube_service


def get_yt_playlist():
    """Get the trash video playlist"""
    youtube = get_authenticated_service()
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=100,
        playlistId=PLAYLIST_ID,
    )
    response = request.execute()
    return response


def insert_video_to_youtube_playlist(video_id):
    """Save a video to the trash playlist"""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = get_authenticated_service()
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": PLAYLIST_ID,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id,
                },
            },
        },
    )
    response = request.execute()
    if response["snippet"]["playlistId"] == PLAYLIST_ID:
        return "success"
    return "failure"


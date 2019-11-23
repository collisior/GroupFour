import os

SCOPE = 'playlist-read-collaborative playlist-modify-private playlist-modify-public ' \
'playlist-read-private user-modify-playback-state user-read-currently-playing ' \
'user-read-playback-state user-read-private user-read-email user-library-modify ' \
'user-library-read user-follow-modify user-follow-read user-read-recently-played ' \
'user-top-read app-remote-control'

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = 'http://0.0.0.0:5000/authorization'
MASTER = 'camillasatte'
COGNITIVE_SERVICE_KEY = os.environ['COGNITIVE_SERVICE_KEY']
COGNITIVE_SERVICE_ENDPOINT = "https://face-emotion.cognitiveservices.azure.com/face/v1.0"
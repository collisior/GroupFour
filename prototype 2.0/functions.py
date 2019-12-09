"""This script contains all of the functions."""
import datetime
import pandas
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
from secret import SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, MASTER
from emotion_song_filters import sad_mood, angry_mood, happy_mood, neutral_mood, fear_mood
from spotify_user_functions import create_playlist


def initializer(username, scope=SCOPE, client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI):
    """This function creates the spotify_object."""
    token = util.prompt_for_user_token(username, scope, client_id,
                                       client_secret, redirect_uri)
    spotify_object = spotipy.Spotify(auth=token)
    return spotify_object


def authorize(response, scope=SCOPE, client_id=CLIENT_ID,
              client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI):
    """This function authorizes the user."""
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                   scope=scope, cache_path='.cache-temp')
    code = sp_oauth.parse_response_code(response)
    t = sp_oauth.get_access_token(code)
    token = util.prompt_for_user_token('temp', scope, client_id,
                                       client_secret, redirect_uri)
    print("TOKEN SPOT", t)
    spotify_object = spotipy.Spotify(auth=token)
    username = spotify_object.current_user()['id']
    open('.cache-' + username, 'w').write(open('.cache-temp', 'r').read())
    return username


def logger(username, event):
    """This function logs attempts."""
    log = pandas.read_csv('log.csv')
    row = pandas.DataFrame([[datetime.datetime.now(), username, event]],
                           columns=['datetime', 'username', 'event'])
    log = row.append(log)
    log.to_csv('log.csv', index=False)


def get_current_user_saved_tracks(sp):
    saved_tracks = []
    results = sp.current_user_saved_tracks()
    total = results['total']
    limit = 50
    offset = 0
    while total > offset+limit:
        results = sp.current_user_saved_tracks(limit, offset)
        offset += limit
        for i in range(limit):
            trackid = results['items'][i]['track']['id']
            saved_tracks.append(trackid)
        if (total-offset-limit)<0:
            limit = total-offset
    return saved_tracks


def get_playlist(sp, emotion, num_of_tracks):
    playlist_to_save = []
    saved_tracks = get_current_user_saved_tracks(sp)

    if emotion=='anger':
        playlist_to_save = angry_mood(sp, saved_tracks)
    elif emotion=='contempt':
        playlist_to_save = sad_mood(sp, saved_tracks)
    elif emotion== 'disgust':
        playlist_to_save = angry_mood(sp, saved_tracks)
    elif emotion == 'fear':
        playlist_to_save = fear_mood(sp, saved_tracks)
    elif emotion== 'happiness':
        playlist_to_save = happy_mood(sp, saved_tracks)
    elif emotion =='neutral':
        playlist_to_save = neutral_mood(sp, saved_tracks)
    elif emotion=='sadness':
        playlist_to_save = sad_mood(sp, saved_tracks)
    elif emotion=='surprise':
        playlist_to_save = happy_mood(sp, saved_tracks)
    return create_playlist(sp, playlist_to_save, emotion, num_of_tracks)





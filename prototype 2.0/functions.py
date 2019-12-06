"""This script contains all of the functions."""
import datetime
import pandas
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
from secret import SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, MASTER


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

    results = sp.current_user_saved_tracks(limit=10, offset=10)
    total = results['total']
    print('  ')
    print('total', total)
    print('  ')
    limit = 50
    offset = 0
    while total > offset+limit:
        results = sp.current_user_saved_tracks(limit, offset)
        offset += limit
        for i in range(limit):
            trackid = results['items'][i]['track']['id']
            print(trackid)
            saved_tracks.append(trackid)
        print(total - offset)
        print(offset)
        if (total-offset-limit)<0:
            print(total-offset-limit, "LIMIT")
            limit = total-offset
            print(limit)


    print("LENGTH   -    ", len(saved_tracks))



def audio_tracks_get(sp):
    playlist_to_save = []
    saved_tracks = []
    get_current_user_saved_tracks(sp)


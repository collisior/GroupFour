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
    sp_oauth.get_access_token(code)
    token = util.prompt_for_user_token('temp', scope, client_id,
                                       client_secret, redirect_uri)
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


def aggregate_top_artists(sp):
    print('...getting your top artists')
    top_artists_name = []
    top_artists_uri = []

    ranges = ['short_term', 'medium_term', 'long_term']
    for r in ranges:
        top_artists_all_data = sp.current_user_top_artists(limit = 50, time_range = r)
        top_artists_data = top_artists_all_data['items']
        for artist_data in top_artists_data:
            if artist_data["name"] not in top_artists_name:
                top_artists_name.append(artist_data['name'])
                top_artists_uri.append(artist_data['uri'])

    followed_artists_all_data = sp.current_user_followed_artists(limit = 50)
    followed_artists_data = (followed_artists_all_data['artists'])
    for artist_data in followed_artists_data["items"]:
        print(artist_data["name"])
        if artist_data["name"] not in top_artists_name:
            top_artists_name.append(artist_data['name'])
            top_artists_uri.append(artist_data['uri'])
    return top_artists_uri
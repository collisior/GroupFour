import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth
import os
import pprint
from flask import Flask, render_template


username="camillasatte"
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, User!"


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"



## SEARCH in SPOTIFY, return results
@app.route('/search')
def client_credential_flow():
    client_credentials_manager = oauth.SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    search_str = 'Rollling Stones Street Love'
    result = sp.search(search_str)
    pprint.pprint(result)
    return result


## spotipy.oauth2.SpotifyClientCredentials
# @app.route('/sp2_tracks')
def get_token_2():
    scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'
    sp2 = spotipy.oauth2.SpotifyClientCredentials(client_id=None, client_secret=None, scope=scope)
    token = sp2.get_access_token()
    return "Done"


def get_token_22():
    scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    redirect_uri = 'https://github.com/collisior/Software-Engineering-Project'
    sp = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, state=None, scope=scope, cache_path=None,
                                proxies=None)

    # return sp.get_access_token(code)


token = ""
@app.route('/set_token')
def set_token():
    scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    redirect_uri = 'https://github.com/collisior/Software-Engineering-Project'
    print("getting token...  ")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    # print("Current token used: " ,token)
    return token


##Return user's saved tracks
@app.route('/list_user_tracks')
def get_track():
    token = set_token()
    list_songs = []
    if token:
        print("USERNAME : ", username)
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks(10)
        for item in results['items']:
            track = item['track']
            track_name = track['name']
            list_songs.append(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)
    str_list_songs = ',      '.join(list_songs)
    return render_template('list_user_tracks.html', your_list=list_songs)
    # return str_list_songs


##
# @app.route('/top_artist')
def top_artists():
    set_token()
    # token =
    if token:
        print("USERNAME : ", username)
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_artists(3)
        for item in results['artists']:
            print(item)
    else:
        print("Can't get token for", username)


# get_track()


if __name__ == "__main__":
    app.run(debug=True)
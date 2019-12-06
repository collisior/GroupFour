"""This script builds the Flask app."""
import pandas
from flask import Flask, request, render_template, redirect
import spotipy.oauth2 as oauth2
from functions import authorize, initializer, audio_tracks_get, logger
from secret import SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


def flask_app():

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/click', methods=['GET'])
    def click():
        logger('button', 'click')
        sp_oauth = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)
        return redirect(sp_oauth.get_authorize_url())

    @app.route('/authorization', methods=['GET'])
    def authorization():
        response = request.url
        username = authorize(response)
        logger(username, 'attempt')
        spotify_object = initializer(username)
        audio_tracks_get(spotify_object)
        logger(username, 'success')
        return render_template('authorized.html')

    return app


if __name__ == '__main__':
    APP = flask_app()
    APP.run(debug=True)

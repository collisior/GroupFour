"""This script builds the Flask app."""
import pandas
from flask import Flask, request, render_template, redirect, send_from_directory
import spotipy.oauth2 as oauth2
from functions import authorize, initializer, aggregate_top_artists, logger
from secret import SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import azure_functions


import os
app = Flask(__name__, static_folder="images")


def flask_app():

    app = Flask(__name__, static_folder="images")
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
        aggregate_top_artists(spotify_object)
        logger(username, 'success')
        return render_template('upload.html')
    
    
    @app.route("/upload", methods=["POST"])
    def upload():
        target = os.path.join(APP_ROOT, 'images/')
        print(target)
        if not os.path.isdir(target):
                os.mkdir(target)
        else:
            print("Couldn't create upload directory: {}".format(target))
        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "/".join([target, filename])
            print ("Accept incoming file:", filename)
            print ("Save it to:", destination)
            upload.save(destination)

    
        # return send_from_directory("images", filename, as_attachment=True)
        return render_template("complete.html", file_path=destination)
    
    @app.route('/upload/<file_path>')
    def send_image(file_path):
        return azure_functions.get_face_emotion_information(file_path)
    #send_from_directory("images", filename)
    #end of upload


    return app


if __name__ == '__main__':
    APP = flask_app()
    APP.run(debug=True)

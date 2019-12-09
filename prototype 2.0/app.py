"""This script builds the Flask app."""
import spotipy
from flask import Flask, request, render_template, redirect, session
import spotipy.oauth2 as oauth2
from functions import authorize, initializer, get_playlist, logger, get_current_user_saved_tracks
from secret import SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from azure_functions import get_face_emotion_information
import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__, static_folder="images")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.secret_key = os.urandom(24)
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     token = db.Column(db.String())

# app.secret_key = b'any random string'

def flask_app():

    app = Flask(__name__, static_folder="images")
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    token = ''

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')


    @app.route('/click', methods=['GET'])
    def click():
        logger('button', 'click')
        sp_oauth = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)
        return redirect(sp_oauth.get_authorize_url())


    @app.route('/authorization', methods=['GET','POST'])
    def authorization():
        response = request.url
        username = authorize(response)
        logger(username, 'attempt')
        spotify_object =initializer(username)
        # session['spotify_object'] = spotify_object
        # get_playlist(spotify_object, 'happiness', 10)
        logger(username, 'success')
        return render_template('upload.html')


    @app.route("/upload", methods=["POST","GET"])
    def upload():

        spotify_object = initializer('camillasatte')
        print('\n\n\n\n\n')
        print("TYPE:", type(spotify_object))

        num_of_tracks = 10
        target = os.path.join(APP_ROOT, 'images/')

        if not os.path.isdir(target):
                os.mkdir(target)
        else:
            print("Couldn't create upload directory: {}".format(target))
        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "".join([target, filename])
            print("Accept incoming file:", filename)
            print("Save it to:", destination)
            upload.save(destination)
            emotion = get_face_emotion_information(destination)
            # spotify_object = session.get('spotify_object', None)
            get_playlist(spotify_object, emotion, num_of_tracks)
            print("DONENENNENENE")
        # return send_from_directory("images", filename, as_attachment=True)
        return render_template("complete.html", file_path=destination)

    @app.route('/upload/<file_path>')
    def send_image(file_path):
        return True
    #send_from_directory("images", filename)
    #end of upload

    return app


if __name__ == '__main__':
    APP = flask_app()
    APP.run(debug=True)

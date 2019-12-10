import random
from datetime import datetime


def current_user_playlist_tracks(spotify, playlist_id=None, fields=None, limit=100, offset=0, market=None):
    pass

def current_user_playlist_create(spotify, playlist_name, public=True):
    pass

def current_user_playlist_add_tracks(spotify, playlist_id, tracks, position=None):
    pass

def create_playlist(sp, filtered_tracks, emotion, num_of_tracks):
    print("...creating playlist")
    user_all_data = sp.current_user()
    user_id = user_all_data["id"]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    playlist_all_data = sp.user_playlist_create(user_id, "Moodify "+str(current_time)+" "+str(emotion))
    playlist_id = playlist_all_data["id"]

    random.shuffle(filtered_tracks)
    sp.user_playlist_add_tracks(user_id, playlist_id, filtered_tracks[0:num_of_tracks])
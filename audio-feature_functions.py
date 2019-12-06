def track_audio_features(spotify, tid):
    trackuri = spotify._get_uri('track', tid)
    return spotify._get("audio-features/%s/track" %trackuri)

def multiple_tracks_audio_features(spotify, tracks):
    ftracks = [spotify._get_uri('track', tid) for tid in tracks]
    return spotify._get("audio-features" % ftracks)
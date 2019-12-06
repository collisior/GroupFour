def track_audio_features(spotify, tid):
    trackuri = spotify._get_uri('track', tid)
    return spotify._get("audio-features/%s/track" %trackuri)
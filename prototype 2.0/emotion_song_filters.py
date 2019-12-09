def sad_mood(sp, tracks):
    saved_tracks = []
    for track in tracks:
        features = sp.audio_features(track)
        danceability = features[0]["danceability"]
        energy = features[0]["energy"]
        valence = features[0]["valence"]
        if valence <= 0.25:
            saved_tracks.append(track)
        elif energy <= 0.25 :
            saved_tracks.append(track)
        elif danceability <= 0.25:
            saved_tracks.append(track)
    return saved_tracks


def angry_mood(sp, tracks):
    saved_tracks = []
    for track in tracks:
        features = sp.audio_features(track)
        energy = features[0]["energy"]
        tempo=features[0]["tempo"]
        if energy >= 0.8 :
            saved_tracks.append(track)
        elif tempo >= 80 and tempo <= 120:
            saved_tracks.append(track)
    return saved_tracks


def happy_mood(sp, tracks):
    saved_tracks = []
    for track in tracks:
        features = sp.audio_features(track)
        energy = features[0]["energy"]
        valence = features[0]["valence"]
        if valence >= 0.75:
            saved_tracks.append(track)
        elif energy <= 0.75 :
            saved_tracks.append(track)
    return saved_tracks


def neutral_mood(sp, tracks):
    saved_tracks = []
    for track in tracks:
        features = sp.audio_features(track)
        energy = features[0]["energy"]
        valence = features[0]["valence"]
        tempo=features[0]["tempo"]
        if valence <= 0.8 and valence >= 0.35:
            saved_tracks.append(track)
        elif energy >= 0.2 and energy <= 0.9:
            saved_tracks.append(track)
        elif tempo>=60 and tempo <= 110:
            saved_tracks.append(track)
    return saved_tracks


def fear_mood(sp, tracks):
    saved_tracks = []
    for track in tracks:
        features = sp.audio_features(track)
        energy = features[0]["energy"]
        valence = features[0]["valence"]
        if valence <= 0.5:
            saved_tracks.append(track)
        elif energy >= 0.2 and energy <= 0.9:
            saved_tracks.append(track)
    return saved_tracks
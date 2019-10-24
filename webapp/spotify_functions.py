import sys
import spotipy
import spotipy.util as util

# shows a user's saved tracks (need to be authenticated via oauth)

def showTracks():
    scope = 'user-library-read'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    count = 0
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks(50) #max to return : 50 tracks

        for item in results['items']:
            count+=1
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)
    print("Total songs: ", count)


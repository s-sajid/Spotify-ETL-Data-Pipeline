import spotipy

# spotify = spotipy.Spotify(client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials())

def get_artists(playlist_uri):
    artists = {}
    playlist_tracks = spotipy.playlist_tracks(playlist_id = playlist_uri)

    for song in playlist_tracks["items"]:
        if song["track"]:
            print(song["track"]["artists"][0]["name"])
            artists[song["track"]["artists"][0]["uri"]] = song["track"]["artists"][0]["name"]
    
    return artists

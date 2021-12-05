import spotipy
import os
from dotenv import load_dotenv
load_dotenv()

spotify = spotipy.Spotify(client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(os.getenv("Client_Id"), os.getenv("Client_Secret")))

def get_artists(playlist_uri):
    artists = {}
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)
    for song in playlist_tracks['items']:
        if song['track']:
            print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    return artists

import spotipy
import csv
import boto3
from datetime import datetime

from config.playlists import spotify_playlist_1
## Insert Tools

spotipy_object = spotipy.Spotify(client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials())

output_dictionary = {
    "Year_Released" : [],
    "Album_Length" : [],
    "Album_Name" : [],
    "Artist" : []
}

PLAYLIST = "Rap_Caviar"
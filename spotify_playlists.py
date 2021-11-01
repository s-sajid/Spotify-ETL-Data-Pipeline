import spotipy
import csv
import boto3
from datetime import datetime

from config.playlists import spotify_playlist_1
## Insert Tools

# spotipy_object = spotipy.Spotify(client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials())



PLAYLIST = "Rap_Caviar"

def gather_data_local():
    output_dictionary = {
    "Year_Released" : [],
    "Album_Length" : [],
    "Album_Name" : [],
    "Artist" : []
}
    with open("Rap_Caviar_Albums.csv", "w") as file:
        header = list( output_dictionary.keys())
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        albums_obtained = []
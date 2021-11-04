import os
import spotipy
import csv
import boto3
from datetime import datetime

from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

spotipy_object = spotipy.Spotify(client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(os.getenv("Client_Id"), os.getenv("Client_Secret")))

from config.playlists import spotify_playlist_1
from tools.playlists import get_artists

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

        artists = get_artists(spotify_playlist_1()[PLAYLIST])
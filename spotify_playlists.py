import os
import spotipy
import csv
import boto3
from datetime import datetime

from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

from config.playlists import spotify_playlist_1
from tools.playlists import get_artists

client_id = os.getenv("Client_Id")
client_secret = os.getenv("Client_Secret")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs("uhdtt9x914rmzvcfxogs72q93", "71sU6agJ13FCerhUW6tlll")

print(len(ids))
print(ids)


PLAYLIST = "rap_caviar"

def gather_data_local():
    
    output_dict = {
    "Year_Released": [],
    "Album_Length": [],
    "Album_Name": [],
    "Artist": []
    }

    with open("rapcaviar_albums.csv", "w") as file:
        header = list( output_dict.keys())
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        albums_obtained = []

        artists = get_artists(spotify_playlist_1()[PLAYLIST])

        for artist in list(artists.keys()):
            print(artist)
            artists_albums = sp.artist_albums(artist, album_type="album", limit = 50)

            for album in artists_albums["items"]:

                if "US" in album["available_markets"]:
                    key = album["name"] + album["artists"][0]["name"] + album["release_date"][:4]

                    if key not in albums_obtained:
                        albums_obtained.append(key)
                        album_data = sp.album(album["uri"])

                        album_length_ms = 0

                        for song in album_data["tracks"]["items"]:
                            album_length_ms = song["duration_ms"] + album_length_ms

                        writer.writerow({"Year Released": album_data["release_date"][:4],
                            "Album Length": album_length_ms,
                            "Album Name": album_data["name"],
                            "Artist": album_data["artists"][0]["name"]})
                    
                        output_dict["Year Released"].append(album_data["release_date"][:4])
                        output_dict["Album Length"].append(album_length_ms)
                        output_dict["Album Name"].append(album_data["name"])
                        output_dict["Artist"].append(album_data["artists"][0]["name"])
    return output_dict
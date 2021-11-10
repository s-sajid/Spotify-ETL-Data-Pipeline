import os
import spotipy
import csv
import boto3
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from config.playlists import spotify_playlist_1
from tools.playlists import get_artists

spotify = spotipy.Spotify(client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(os.getenv("Client_Id"), os.getenv("Client_Secret")))


file_name = "rapcaviar_albums.csv"
abs_file_path = os.path.join(os.getenv("data_directory"), file_name)

PLAYLIST = "Rap_Caviar"

def gather_data_local():
    
    output_dict = {
        "Year Released": [],
        "Album Length": [],
        "Album Name": [],
        "Artist": []
    }


    with open(abs_file_path, "w") as file:
        header = list(output_dict.keys())
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        albums_obtained = []

        artists = get_artists(spotify_playlist_1()[PLAYLIST])

        for artist in list(artists.keys()):
            print(artist)
            artists_albums = spotify.artist_albums(artist, album_type="album", limit=50)
            
            for album in artists_albums["items"]:
                if "US" in album["available_markets"]:
                    key = album["name"] + album["artists"][0]["name"] + album["release_date"][:4]

                    if key not in albums_obtained:
                        albums_obtained.append(key)
                        album_data = spotify.album(album["uri"])
                        
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

gather_data_local()

def gather_data():

    with open(abs_file_path, "w") as file:
        header = ["Year Released", "Album Length", "Album Name", "Artist"]
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        artists = get_artists(spotify_playlist_1()[PLAYLIST])

        for artist in artists.keys():
            artists_albums = spotify.artist_albums(artist, album_type = "album", limit = 50)

            for album in artists_albums["items"]:
                if "US" in artists_albums["items"][0]["available_markets"]:
                    album_data = spotify.album(album["uri"])

                    album_length_ms = 0

                    for song in album_data["tracks"]["items"]:
                        album_length_ms = song["duration_ms"] + album_length_ms

                    writer.writerow({"Year Released": album_data["release_date"][:4],
                                    "Album Length": album_length_ms,
                                    "Album Name": album_data["name"],
                                    "Artist": album_data["artists"][0]["name"]})

    s3_res =boto3.resource("s3")
    date = datetime.now()
    filename = f"{date.year}/{date.month}/{date.day}/rapcaviar_albums.csv"
    
    response = s3_res.Object("spotify_analysis_data", filename).upload_file(abs_file_path)

    return response

def lambda_handler(event, context):
    gather_data()

# if __name__ == "__main__":
#     data = gather_data()
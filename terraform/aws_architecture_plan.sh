# terraform init

cp -r C:/Users/sdsaj/Anaconda3/Lib/site-packages/spotipy ../lambda_payloads/playlist_payload/spotipy
cp -r C:/Users/sdsaj/Anaconda3/Lib/site-packages/requests ../lambda_payloads/playlist_payload/

cp C:/Users/sdsaj/Desktop/Python/Spotify_Data_Pipeline/spotify_playlists.py ../lambda_payloads/playlist_payload/
cp C:/Users/sdsaj/Desktop/Python/Spotify_Data_Pipeline/config/* ../lambda_payloads/playlist_payload/config
cp C:/Users/sdsaj/Desktop/Python/Spotify_Data_Pipeline/tools/* ../lambda_payloads/playlist_payload/tools

# terraform validate

# terraform plan

# terraform apply
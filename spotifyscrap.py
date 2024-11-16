import pandas as pd
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set your Spotify credentials (replace with your own)
load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
print(sp)
# # Define playlist ID you want to scrap
# playlist_ids = ["37i9dQZEVXbObFQZ3JLcXt","37i9dQZEVXbKXQ4mDTEBXq","37i9dQZEVXbNxXF4SkHj9F","37i9dQZEVXbNBz9cRCSFkY","37i9dQZEVXbLZ52XmnySJg"]

# # Indonesia : https://open.spotify.com/playlist/37i9dQZEVXbObFQZ3JLcXt?si=1cc77672eba846ec
# # Japan : https://open.spotify.com/playlist/37i9dQZEVXbKXQ4mDTEBXq?si=1808186a85854ab1
# # South Korea : https://open.spotify.com/playlist/37i9dQZEVXbNxXF4SkHj9F?si=94b55a11bd864dd2
# # Philippines : https://open.spotify.com/playlist/37i9dQZEVXbNBz9cRCSFkY?si=e2f49b7f8c954bf1
# # India : https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg?si=e3eaf8cad26c4680

# # Initialize list to store final data
# final_data = []

# # Loop through each playlist and Fetch playlist metadata
# for playlist_id in playlist_ids:
#     playlist_data = sp.playlist(playlist_id)
#     playlist_name = playlist_data["name"]
#     playlist_followers = playlist_data["followers"]["total"]

#     # Fetch tracks in playlist
#     tracks = sp.playlist_tracks(playlist_id)

# # Loop through each track to get details and audio features
#     for track_item in tracks["items"]:
#         track = track_item["track"]
#         track_id = track["id"]
#         track_name = track["name"]
#         artist_name = track["artists"][0]["name"]
#         artist_id = track["artists"][0]["id"]
#         album_name = track["album"]["name"]
#         album_type = track["album"]["album_type"]
#         album_release_date = track["album"]["release_date"]
#         duration_ms = track["duration_ms"]
#         popularity = track["popularity"]

#         # Fetch artist details to get genre information
#         artist_data = sp.artist(artist_id)
#         genres = artist_data["genres"]  # Get genres (list)

#         # Fetch audio features for the track
#         audio_features = sp.audio_features(track_id)[0]
        
#         # Check if audio features are available
#         if audio_features:
#             danceability = audio_features["danceability"]
#             energy = audio_features["energy"]
#             tempo = audio_features["tempo"]
#             valence = audio_features["valence"]
#             mode_majorminor = audio_features["mode"]
#         else:
#             danceability = energy = tempo = valence = mode_majorminor = None  # Handle missing audio features
        
#         # Store all data in a dictionary and append to list
#         track_data = {
#             "playlist_name": playlist_name,
#             "playlist_followers": playlist_followers,
#             "track_name": track_name,
#             "artist_name": artist_name,
#             "artist_genres": genres,
#             "album_name": album_name,
#             "album_type": album_type,
#             "album_release_date": album_release_date,
#             "duration_ms" : duration_ms,
#             "popularity": popularity,
#             "danceability": danceability,
#             "energy": energy,
#             "tempo": tempo,
#             "valence" : valence,
#             "mode_majorminor" : mode_majorminor
#         }
#         final_data.append(track_data)

# # Convert to DataFrame
# df_playlist_data = pd.DataFrame(final_data)

# # Save DataFrame to a CSV file
# df_playlist_data.to_csv("spotify_playlist_data.csv", index=False)
# print("Data saved to spotify_playlist_data.csv")


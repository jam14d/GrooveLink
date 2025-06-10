import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

track_id = "11dFghVXANMlKmJXsNCbNl"  # a known working track (Daft Punk – Get Lucky)

try:
    feature = sp.audio_features([track_id])[0]
    print("Success:", feature)
except Exception as e:
    print("Failed:", e)

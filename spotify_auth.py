import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load the .env file
print("Loading .env...")
load_dotenv()

def get_spotify_client():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    print("CLIENT ID:", client_id)  # TEMP DEBUG

    if not client_id or not client_secret:
        raise Exception("Missing SPOTIPY_CLIENT_ID or SPOTIPY_CLIENT_SECRET")

    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    token = auth_manager.get_access_token()
    print("Spotify Token:", token)

    return spotipy.Spotify(auth_manager=auth_manager)

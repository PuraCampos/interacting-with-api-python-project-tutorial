import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
con = spotipy.Spotify(auth_manager=auth_manager)

artist_sp = 'spotify:artist:7qJXYbBDibZ1Zixi89aUnw'

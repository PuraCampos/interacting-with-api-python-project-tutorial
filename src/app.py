import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt


load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

artist_ID = "64tJ2EAv1R6UaZqc4iOCyj"

result = sp.artist_top_tracks(artist_ID, country="JP")
if result: 
    tracks = result["tracks"]
    tracks = [
        {
            "name": track["name"],
            "popularity": track["popularity"],
            "duration_ms": (track["duration_ms"] / (1000 * 60)) 
        }
        for track in tracks
    ]

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(["popularity"], inplace = True)

print(tracks_df.head(5))

sns.set_theme(style="whitegrid")
cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)

scatter_plot = sns.scatterplot(data = tracks_df, x = "popularity", y = "duration_ms")

plt.xlabel("Popularity")
plt.ylabel("Duration (minutes)")
plt.title("YOASOBI" "\nRelation between Popularity and Duration of Top Tracks")
plt.savefig("YOASOBI_top_tracks.png")

plt.show()


import pandas as pd
import lib.functions as f
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import random
from bs4 import BeautifulSoup
import re
import pickle

def song_recommender(sp, songs, artists):
    try:
        ids = f.search_song(sp, songs, artists)
        data = f.get_audio_features(sp, ids)
        data = data.drop(["key", "mode", "type", "id", "uri", "track_href", "analysis_url", "time_signature"], axis = 1)
        scaler = f.load("./transformer/scaler.pickle")
        data_norm = scaler.transform(data)
        kmeans_9 = f.load("./models/kmeans_9.pickle")
        cluster = kmeans_9.predict(data_norm)
        songs_final = pd.read_csv('./data/songs_with_clusters.csv')
        hot = list(songs_final[songs_final["song_label"] == "H"]["id"])
        not_hot = list(songs_final[songs_final["song_label"] == "R"]["id"])
        if ids in hot:
            x = songs_final[(songs_final["clusters_kmeans"] == cluster[0]) & (songs_final["song_label"] == "H")]
            x = x[x["id"] != ids[0]]
            recommended_song = x.sample(n=1)
            return print("Recommended song for user: ", list(recommended_song[["song", "artist"]].iloc[0])[0],"/ Song artist: ", list(recommended_song[["song", "artist"]].iloc[0])[1])
        else:
            y = songs_final[(songs_final["clusters_kmeans"] == cluster[0]) & (songs_final["song_label"] == "H")]
            y = y[y["id"] != ids[0]]
            recommended_song2 = y.sample(n=1, replace = False)
            return print("Recommended song for user: ", list(recommended_song2[["song", "artist"]].iloc[0])[0],"/ Song artist: ", list(recommended_song2[["song", "artist"]].iloc[0])[1])
    except:
        return "Song or artist not found"
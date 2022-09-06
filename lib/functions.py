import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pickle


def scrape_hot100(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        song = []
        artist = []
        for elem in soup.select("li.o-chart-results-list__item > h3"):
            song.append(elem.get_text().strip())
        for elem in soup.select("li.o-chart-results-list__item > span"):
            x = elem.get_text().strip()
            if re.match("\d{1,}|-|NEW|RE-\nENTRY", x):
                pass
            else:
                artist.append(x)
        top_100 = pd.DataFrame({"song": song, "artist":artist})
        return top_100


def generate_random_songs(x, y):
    y = y[['title', 'artist']]
    y.columns = ["song", "artist"]
    y = y.drop_duplicates( subset = ['song', 'artist']).reset_index(drop=True) 
    y = y.sample(n=3000, replace=False, random_state = 100).reset_index(drop=True)
    for i in range(len(x)):
        for j in range(len(y)):
            if list(x.iloc[i]) == list(y.iloc[j]):
                y = y.drop(y.iloc[j], axis = 0)
            else:
                pass                 
    return y

def search_song_good(sp, songs, artists):
    id_song = []
    for song, artist in zip(songs, artists):
        try:
            results = sp.search(q="track:"+song+" artist:"+artist, limit=1)
            ids = results['tracks']['items'][0]["id"]
            id_song.append(ids)
        except:
            ids = ""
            id_song.append(ids)
    return id_song


def search_song(sp, songs, artists):
    id_song = []
    for song, artist in zip(songs, artists):
        try:
            results = sp.search(q="track:"+song+" artist:"+artist, limit=1)
            ids = results['tracks']['items'][0]["id"]
            id_song.append(ids)
        except:
            ids = ""
            id_song.append(ids)
    return id_song


def get_audio_features(sp, list_song_id):
    data = pd.DataFrame(columns=['danceability', 'energy', 'key', "loudness", "mode",
                          "speechiness", "acousticness", "instrumentalness", "liveness",
                          "valence", "tempo", "type", "id", "uri", "track_href", "analysis_url",
                          "duration_ms", "time_signature"])
    for i in list_song_id:
        try:
            my_dict = sp.audio_features([i])[0]
            df = pd.DataFrame.from_dict(my_dict, orient = "index").T
            data = pd.concat([data, df], axis = 0).reset_index(drop = True)
        except:
            pass
    return data 


def add_audio_features(df, audio_features_df):
    data = pd.concat([df, audio_features_df], axis = 1)
    return data

def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as file: 
            return pickle.load(file) 
    except FileNotFoundError: 
        print("File not found!")


# Gnod project

Song recommender 

### Objective

The aim of this project was to create a song recommender using unsupervised learning. A song input by the user would first be filtered on whether the song in on the top 100 of the billboard list. In this case, the song recommender will return to the user a similar song based on the results of the unsupervised learning model (Kmeans), this song will also belong to the top 100 songs in the billboard list. In case the input song in not in the top 100, the song recommender will return a similar song based on a random song list. 

### Data sources

Data used in this project was obtained by web scraping the top 100 songs on Tuesday 23.08.2022:  [https://www.billboard.com/charts/hot-100/](https://www.billboard.com/charts/hot-100/)

A list of random songs was obtained from kaggle: [https://www.kaggle.com/datasets/sumitmohod22/songs-data-set?resource=download](https://www.kaggle.com/datasets/sumitmohod22/songs-data-set?resource=download)

A list of audio features for each song was obtained using the spotify API

### Results

The generated song recommender is found in: ./notebooks/[song_recommender.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/song_recommender.ipynb)

### Languages and tools

Python

Jupyter notebook

### Folders in this project

- data: data generated in the jupyter notebooks. The list of random songs from Kaggle is not included.
- models: fitted kmeans model with 9 clusters
- notebooks: includes eight notebooks
    - [lab-web-scraping-single-page.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/lab-web-scraping-single-page.ipynb): code top download hot 100 songs from the billboard webpage
    - [lab-not-hot-songs.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/lab-not-hot-songs.ipynb): code to generate a list of random songs
    - [spotify_API.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/spotify_API.ipynb): code to obtain audio features of both lists of songs
    - [Dataframe_for_modeling.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/Dataframe_for_modeling.ipynb): code to generate a concatenated dataframe of both hot 100 and random songs, with a new feature column with label “H” (hot) and “R” (random)
    - [Gaussian_modeling .ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/Gaussian_modeling%20.ipynb): code for gaussian mixture model
    - [clustering_KMeans.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/clustering_KMeans.ipynb): code for kmeans model
    - [song_recommender_code.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/song_recommender_code.ipynb): code to define the function of the song_recommender
    - [song_recommender.ipynb](http://localhost:8888/notebooks/Desktop/Ironhack/Week6/Gnod_project_week6/notebooks/song_recommender.ipynb): final product
- scalers: fitted scaler
- models: fitted gaussian and kmeans models
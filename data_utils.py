import pandas as pd
import streamlit as st


@st.cache_data
def load_spotify_data():
    """
    Carrega o dataset do Spotify a partir de data/spotify.csv
    e faz alguns ajustes básicos.
    """
    df = pd.read_csv("data/spotify.csv")

    # Remover coluna de índice gerada na exportação
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Garantir nomes "limpos"
    df.columns = [c.strip() for c in df.columns]

    # Colunas que sabemos que existem nesse dataset:
    # ['track_id', 'artists', 'album_name', 'track_name',
    #  'popularity', 'duration_ms', 'explicit', 'danceability', 'energy',
    #  'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    #  'instrumentalness', 'liveness', 'valence', 'tempo',
    #  'time_signature', 'track_genre']

    numeric_candidates = [
        "popularity",
        "duration_ms",
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
    ]
    df.attrs["numeric_candidates"] = [c for c in numeric_candidates if c in df.columns]

    # Guardar colunas úteis em atributos
    df.attrs["genre_col"] = "track_genre" if "track_genre" in df.columns else None
    df.attrs["artist_col"] = "artists" if "artists" in df.columns else None

    return df

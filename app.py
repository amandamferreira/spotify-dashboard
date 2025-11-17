# app.py
import streamlit as st
from data_utils import load_spotify_data

st.set_page_config(
    page_title="Dashboard Spotify – Análise de Músicas",
    layout="wide"
)

df = load_spotify_data()

st.title("🎧 Dashboard Spotify – Análise de Músicas")

st.markdown("""
### 🎯 Objetivo do dashboard

Este dashboard foi desenvolvido para **explorar visualmente um conjunto de músicas do Spotify**, 
permitindo identificar **padrões, tendências e relações** entre popularidade e características 
das faixas (como *danceability*, *energy*, *valence*, entre outras).

---

### 🧭 Como navegar entre as seções

Use o **menu de páginas** na lateral esquerda para acessar:

- **Visão Geral**: visão inicial do dataset, com distribuição de gêneros e popularidade.
- **Análises por Categoria**: comparação de métricas por gênero, artista ou outra categoria.
- **Características das Músicas**: análise de como as características de áudio se relacionam.
- **Correlações**: relação entre as variáveis numéricas (ex.: energy x danceability).

---

### 🎚️ Como os filtros influenciam os dados

Em cada página, você encontrará filtros como:

- Seleção de **gênero** ou **artista**;
- Limite de **quantidade de categorias** exibidas;
- Escolha de **métricas numéricas** (popularidade, energy, danceability etc.).

Esses filtros **alteram dinamicamente os gráficos e tabelas**, permitindo focar em partes específicas
do dataset e descobrir insights sobre as músicas do Spotify.
""")

st.markdown("---")

st.subheader("👀 Pré-visualização do dataset")
st.dataframe(df.head())

num_rows, num_cols = df.shape
st.caption(f"O dataset possui **{num_rows} linhas** e **{num_cols} colunas**.")

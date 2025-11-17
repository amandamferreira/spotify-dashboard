import streamlit as st
import plotly.express as px
from data_utils import load_spotify_data

df = load_spotify_data()
genre_col = df.attrs.get("genre_col", None)

st.title("🎛 Características das Músicas")

st.sidebar.header("Filtros – Características")

# Filtro por gênero (opcional)
if genre_col and genre_col in df.columns:
    genres = sorted(df[genre_col].unique())
    selected_genres = st.sidebar.multiselect(
        "Filtrar por gêneros (opcional):",
        options=genres,
        default=genres[:5]
    )
    if selected_genres:
        df = df[df[genre_col].isin(selected_genres)]

# Filtro por faixa de popularidade
if "popularity" in df.columns:
    min_pop = int(df["popularity"].min())
    max_pop = int(df["popularity"].max())
    pop_range = st.sidebar.slider(
        "Filtrar por faixa de popularidade:",
        min_value=min_pop,
        max_value=max_pop,
        value=(min_pop, max_pop)
    )
    df = df[(df["popularity"] >= pop_range[0]) & (df["popularity"] <= pop_range[1])]

col1, col2 = st.columns(2)

# Gráfico 1 – Dispersão danceability x energy
with col1:
    st.markdown("### 💃 Danceability x Energy")
    if "danceability" in df.columns and "energy" in df.columns:
        fig_scatter = px.scatter(
            df,
            x="danceability",
            y="energy",
            color="valence" if "valence" in df.columns else None,
            title="Relação entre danceability e energy (cor = valence, se disponível)",
            opacity=0.7
        )
        fig_scatter.update_layout(xaxis_title="Danceability", yaxis_title="Energy")
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.info("As colunas 'danceability' e/ou 'energy' não foram encontradas no dataset.")

# Gráfico 2 – Histograma de duração
with col2:
    st.markdown("### ⏱ Distribuição da duração das músicas (ms)")
    if "duration_ms" in df.columns:
        fig_dur = px.histogram(
            df,
            x="duration_ms",
            nbins=40,
            title="Histograma da duração das músicas (em milissegundos)"
        )
        fig_dur.update_layout(xaxis_title="Duração (ms)", yaxis_title="Quantidade")
        st.plotly_chart(fig_dur, use_container_width=True)
    else:
        st.info("A coluna 'duration_ms' não foi encontrada no dataset.")

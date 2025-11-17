# pages/1_Visao_Geral.py
import streamlit as st
import plotly.express as px
from data_utils import load_spotify_data

df = load_spotify_data()

st.title("📌 Visão Geral do Dataset Spotify")

st.sidebar.header("Filtros – Visão Geral")

genre_col = df.attrs.get("genre_col", None)

col1, col2 = st.columns(2)

# Gráfico 1 – Top gêneros
with col1:
    st.markdown("### 🎼 Top gêneros (mais frequentes)")
    if genre_col and genre_col in df.columns:
        top_n = st.sidebar.slider(
            "Quantos gêneros exibir?",
            min_value=5,
            max_value=30,
            value=10
        )
        genre_counts = df[genre_col].value_counts().head(top_n).reset_index()
        genre_counts.columns = [genre_col, "count"]

        fig_genres = px.bar(
            genre_counts,
            x=genre_col,
            y="count",
            title=f"Top {top_n} gêneros mais frequentes",
        )
        fig_genres.update_layout(xaxis_title="Gênero", yaxis_title="Quantidade")
        st.plotly_chart(fig_genres, use_container_width=True)
    else:
        st.info("Nenhuma coluna de gênero encontrada automaticamente no dataset.")

# Gráfico 2 – Histograma de popularidade
with col2:
    st.markdown("### ⭐ Distribuição de popularidade")
    if "popularity" in df.columns:
        fig_pop = px.histogram(
            df,
            x="popularity",
            nbins=30,
            title="Histograma da popularidade das músicas"
        )
        fig_pop.update_layout(xaxis_title="Popularidade", yaxis_title="Frequência")
        st.plotly_chart(fig_pop, use_container_width=True)
    else:
        st.info("A coluna 'popularity' não foi encontrada no dataset.")

st.markdown("---")
st.markdown("### 📊 Estatísticas descritivas das colunas numéricas")
st.write(df.describe())

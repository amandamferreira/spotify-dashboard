# pages/2_Analises_Por_Categoria.py
import streamlit as st
import plotly.express as px
from data_utils import load_spotify_data

df = load_spotify_data()

st.title("📂 Análises por Categoria")

st.sidebar.header("Filtros – Categoria")

categorical_cols = [c for c in df.columns if df[c].dtype == "object"]
numeric_cols = df.attrs.get("numeric_candidates", [])
if not numeric_cols:
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

if not categorical_cols or not numeric_cols:
    st.warning("É necessário ter ao menos uma coluna categórica e uma numérica no dataset.")
    st.stop()

cat_col = st.sidebar.selectbox(
    "Selecione a coluna categórica (ex.: track_genre, artists):",
    options=categorical_cols,
    index=categorical_cols.index("track_genre") if "track_genre" in categorical_cols else 0
)

num_col = st.sidebar.selectbox(
    "Selecione a coluna numérica (ex.: popularity, energy, danceability):",
    options=numeric_cols,
    index=numeric_cols.index("popularity") if "popularity" in numeric_cols else 0
)

st.markdown(f"### Média de `{num_col}` por `{cat_col}`")

grouped = df.groupby(cat_col)[num_col].mean().reset_index().sort_values(num_col, ascending=False)

top_n_cat = st.sidebar.slider(
    "Limitar ao Top N categorias (para visualizar melhor):",
    min_value=5,
    max_value=min(30, len(grouped)),
    value=min(10, len(grouped))
)

grouped_top = grouped.head(top_n_cat)

fig_mean = px.bar(
    grouped_top,
    x=cat_col,
    y=num_col,
    title=f"Média de {num_col} por {cat_col} (Top {top_n_cat})"
)
fig_mean.update_layout(xaxis_title=cat_col, yaxis_title=f"Média de {num_col}")
st.plotly_chart(fig_mean, use_container_width=True)

st.markdown("---")
st.markdown(f"### Distribuição de `{num_col}` por `{cat_col}` (Boxplot)")

fig_box = px.box(
    df,
    x=cat_col,
    y=num_col,
    title=f"Distribuição de {num_col} por {cat_col}"
)
fig_box.update_layout(xaxis_title=cat_col, yaxis_title=num_col)
st.plotly_chart(fig_box, use_container_width=True)

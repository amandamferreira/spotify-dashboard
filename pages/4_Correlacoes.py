import streamlit as st
import plotly.express as px
from data_utils import load_spotify_data

df = load_spotify_data()

st.title("🔗 Correlações entre Variáveis")

st.sidebar.header("Filtros – Correlações")

numeric_cols = df.attrs.get("numeric_candidates", [])
if not numeric_cols:
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

if len(numeric_cols) < 2:
    st.warning("São necessárias pelo menos duas colunas numéricas para analisar correlações.")
    st.stop()

selected_cols = st.sidebar.multiselect(
    "Selecione as colunas numéricas para a matriz de correlação:",
    options=numeric_cols,
    default=numeric_cols[: min(6, len(numeric_cols))]
)

if len(selected_cols) < 2:
    st.warning("Selecione pelo menos duas colunas numéricas.")
    st.stop()

st.markdown("### 📌 Matriz de correlação")

corr_matrix = df[selected_cols].corr()

fig_corr = px.imshow(
    corr_matrix,
    text_auto=True,
    title="Matriz de correlação entre variáveis numéricas selecionadas"
)
st.plotly_chart(fig_corr, use_container_width=True)

st.markdown("---")
st.markdown("### 📉 Dispersão entre duas variáveis")

x_col = st.sidebar.selectbox("Eixo X:", options=selected_cols, index=0)
y_col = st.sidebar.selectbox("Eixo Y:", options=selected_cols, index=min(1, len(selected_cols) - 1))

fig_scatter = px.scatter(
    df,
    x=x_col,
    y=y_col,
    trendline="ols",  # precisa de statsmodels instalado
    title=f"Dispersão entre {x_col} e {y_col} com linha de tendência"
)
fig_scatter.update_layout(xaxis_title=x_col, yaxis_title=y_col)
st.plotly_chart(fig_scatter, use_container_width=True)

import streamlit as st
import pandas as pd

# Dados das espécies
dados = {
    'Espécie': ['Eucalipto', 'Pinus'],
    'Peso Seco (kg/m³)': [550, 520],
    'Peso Úmido (kg/m³)': [611.11, 611.11],
    'Densidade (kg/m³)': [943.20, 520.00]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Título do Dashboard
st.title("Dashboard de Pinus e Eucalipto")

# Exibir tabela
st.subheader("Tabela de Dados")
st.dataframe(df)

# Gráfico de barras
st.subheader("Gráfico de Densidade")
st.bar_chart(df.set_index('Espécie')['Densidade (kg/m³)'])

# Gráfico de Peso Seco e Úmido
st.subheader("Gráfico de Peso Seco e Úmido")
st.bar_chart(df.set_index('Espécie')[['Peso Seco (kg/m³)', 'Peso Úmido (kg/m³)']])

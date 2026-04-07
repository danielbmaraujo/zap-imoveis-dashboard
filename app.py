import streamlit as st
import pandas as pd 

st.title("Dashboard de Imóveis - Fortaleza")

df = pd.read_csv('imoveis.csv')
st.dataframe(df)

bairros = ['Todos'] + sorted(df['bairro'].unique().tolist())
bairro_selecionado = st.selectbox('Filtrar por bairro:', bairros)

if bairro_selecionado != 'Todos':
    df = df[df['bairro'] == bairro_selecionado]

#Exebir grafico 
    st.subheader("Quantidade de imóveis por bairro")
contagem = df['bairro'].value_counts()
st.bar_chart(contagem)
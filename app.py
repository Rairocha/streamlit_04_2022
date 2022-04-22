import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.write('Site do streamlit')

file_input = st.file_uploader('Coloque o csv aqui')

if file_input:
    df = pd.read_csv(file_input)
    if st.checkbox('Ver head'):
        n = st.number_input('Quantas linhas você quer ver?',min_value=1, step=1)
        selected_columns = st.multiselect('Que colunas você quer?',df.columns)
        if len(selected_columns)==0:
            st.write(df.head(n))
        else:
            st.write(df.head(n)[selected_columns])
    if st.checkbox('Ver Filtro'):
        selected_filter = st.selectbox('Qual a coluna do filtro?', df.columns)
        selected_type = st.selectbox('Qual tipo do filtro?', df[selected_filter].unique())
        st.write(df.loc[df[selected_filter] == selected_type ])
    if st.checkbox('Ver grafico'):
        fig1, ax1 = plt.subplots(figsize=(20,10))
        sns.scatterplot(x='Attack', y = 'Defense', data=df,ax=ax1)
        st.pyplot(fig1)
        fig2 = px.scatter(df,x='Attack',y='Defense')
        st.plotly_chart(fig2)
else:
    st.write('Coloca o arquivo!!!')



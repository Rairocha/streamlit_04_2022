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
    if st.checkbox('Ver Tableau'):
        tableau_html="<div class='tableauPlaceholder' id='viz1650648801635' style='position: relative'><noscript><a href='#'><img alt='SUMMARY METRICS ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Em&#47;Embed-HawaiiCOVID-19SummaryMetricsFinal&#47;SUMMARYMETRICS&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Embed-HawaiiCOVID-19SummaryMetricsFinal&#47;SUMMARYMETRICS' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Em&#47;Embed-HawaiiCOVID-19SummaryMetricsFinal&#47;SUMMARYMETRICS&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650648801635');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1040px';vizElement.style.height='747px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1040px';vizElement.style.height='747px';} else { vizElement.style.width='100%';vizElement.style.height='1702px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
        st.components.v1.html(tableau_html,width=2000,height=1000)
else:
    st.write('Coloca o arquivo!!!')



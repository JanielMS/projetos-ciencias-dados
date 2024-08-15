import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly_express as px
import altair as alt

st.set_page_config(page_title='Tutorial de Graficos',
                    page_icon=':smile:',
                    layout='wide')

# emojis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

st.title('😎  :blue[Gráficos básicos no Streamlit]')

df = sns.load_dataset('tips')
with st.expander('Clique para visualizar os dados', icon='✅'): # :white_check_mark:
    st.dataframe(df.head())

st.sidebar.image(image='https://images.ctfassets.net/23aumh6u8s0i/2Qhstbnq6i34wLoPoAjWoq/9f66f58a22870df0d72a3cbaf77ce5b6/streamlit_hero.jpg')
options = st.sidebar.selectbox('Menu', options=['Matplotlib', 'Plotly', 'Altair'])

if options == 'Matplotlib':
    st.subheader(':blue[Matplotlib]' + '✔️')    # :heavy_check_mark:
    st.write('Para conhecer mais sobre a biblioteca :blue[Matplotlib]? Clique [aqui](https://matplotlib.org/stable/index.html)')
    st.write('Para conhecer mais sobre a biblioteca :red[Seaborn]? Clique [aqui](https://seaborn.pydata.org/)')

    with st.expander('Clique para visualizar os graficos'):

        col1, col2 = st.columns(2)

        with col1:
            st.write('#### Barras 📊')     # :bar_chart:
            f1, ax1 = plt.subplots(figsize=(8, 4))
            ax1 = sns.barplot(data=df, x='day', y='total_bill',
                             hue='sex')
            plt.title('Gráfico de Barras - Tips Dataset')
            st.pyplot(f1, use_container_width=True)
            
            st.write('#### Histograma 📶') # :signal_strength:
            f2, ax2 = plt.subplots(figsize=(8, 4))
            ax2 = sns.histplot(data=df, x='total_bill', kde=True, hue='sex')
            plt.title('Histograma - Tips Dataset')
            st.pyplot(f2, use_container_width=True)

    with st.expander('Clique para visualizar os graficos'):
        with col2:
            st.write('#### Boxplot ⏹️')    # :black_square_for_stop:
            f3, ax3 = plt.subplots(figsize=(8, 4))
            ax3 = sns.boxplot(data=df, x='sex', y='tip', hue='day')
            plt.title('Boxplot - Tips Dataset')
            st.pyplot(f3)

            st.write('#### Dispersao 📈')  # :chart_with_upwards_trend:
            f4, ax4 = plt.subplots(figsize=(8, 4))
            sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex')
            plt.title('Grafico de dispersao - Tips Dataset')
            st.pyplot(f4)

elif options == 'Plotly':
    st.subheader(':green[Plotly]')
    st.write('Para conhecer mais sobre a biblioteca :green[Plotly]? Clique [aqui](https://community.plotly.com/)')

    st.write('#### Barras')
    fig1 = px.bar(data_frame=df, x='day', y='total_bill', color='sex',
                  color_discrete_sequence=['dodgerblue','darkorange'],
                  labels=['F', 'M'])
    #fig1.update_traces(marker_color=['red', 'green'])
    st.plotly_chart(fig1, use_container_width=True)

    st.write('#### Histograma')
    fig2 = px.histogram(data_frame=df, x='total_bill', color='sex',
                        color_discrete_sequence=['dodgerblue', 'darkorange'],
                        marginal='box')
    st.plotly_chart(fig2)

    st.write('#### Boxplot')
    fig3 = px.box(data_frame=df, x='day', y='total_bill', color='sex',
                  color_discrete_sequence=['dodgerblue', 'darkorange'])
    st.plotly_chart(fig3)

    st.write('#### Dispersao')
    fig4 = px.scatter(data_frame=df, x='total_bill', y='tip', color='sex',
                      color_discrete_sequence=['dodgerblue', 'darkorange'])
    st.plotly_chart(fig4)

elif options == 'Altair':
    st.subheader(':orange[Altair]')
    st.write('Para conhecer mais sobre a biblioteca :orange[Altair]? Clique [aqui](https://altair-viz.github.io/index.html)')
    st.write('#### Barras')
    bar_chart = alt.Chart(data=df, width=10).mark_bar().encode(
        x='day', y='total_bill', 
        color=alt.Color(shorthand='sex',
                         scale=alt.Scale(domain=['Male', 'Female'],
                                          range=['dodgerblue', 'darkorange']))
    )
    st.altair_chart(bar_chart, use_container_width=True)

    st.write('#### Histograma')
    hist_chart = alt.Chart(df, width=10).mark_bar().encode(
        alt.X('total_bill', bin=True),
        alt.Y('count()'),
        color=alt.Color(shorthand='sex',
                         scale=alt.Scale(domain=['Male', 'Female'],
                                          range=['dodgerblue', 'darkorange']))
    )
    st.altair_chart(hist_chart, use_container_width=True)

    st.write('#### Boxplot')
    box_chart = alt.Chart(data=df).mark_boxplot().encode(
        x='day',
        y='total_bill',
        color=alt.Color(shorthand='sex',
                         scale=alt.Scale(domain=['Male', 'Female'],
                                          range=['dodgerblue', 'darkorange']))
    )
    st.altair_chart(box_chart, use_container_width=True)

    st.write('#### Dispersao')
    scatter_chart = alt.Chart(df).mark_point().encode(
        x='total_bill',
        y='tip',
        color=alt.Color(shorthand='sex',
                         scale=alt.Scale(domain=['Male', 'Female'],
                                          range=['dodgerblue', 'darkorange']))
    )
    st.altair_chart(scatter_chart, use_container_width=True)

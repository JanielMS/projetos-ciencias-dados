import streamlit as st 

# trabalhando com arquivos de midia
st.title('Trabalhando com Arquivos de Midia')

## arquivos de imagens
st.text('Imagem local')
local_img = st.image('vegeta_in_the_rain.jpg', width=300)

st.text('Imagem url')
web_img = st.image(
    'https://i.pinimg.com/originals/e6/40/73/e64073abe42ae193e6d7fbfce745336b.jpg',
    width=400)

## arquivos de audio
st.text('Arquivos de audio')
audio = st.audio('audio.mp3')

## arquivos de video
st.text('Arquivos de video')
video = st.video('video.mp4')

narutin = st.video('https://www.youtube.com/watch?v=wEWF2xh5E8s')
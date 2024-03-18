import streamlit as st
from PIL import Image
from gtts import gTTS
import random
import time
import os
from googletrans import Translator

# Lista de nomes e caminhos das imagens
image_data = [
    {"nome": "Morango", "imagem": "morango.jpg"},
    {"nome": "Abacaxi", "imagem": "abacaxi.jpg"},
    {"nome": "Banana", "imagem": "banana.jpg"}
]

# Estado para controlar o destaque da imagem
selected_image = None

# Função para traduzir o nome da fruta para o inglês e vocalizar
def translate_and_play_mp3(name):
    translator = Translator()
    translated_name = translator.translate(name, dest='en').text
    tts = gTTS(text=translated_name, lang='en')
    tts.save("translated_fruit.mp3")
    st.audio("translated_fruit.mp3", format="audio/mp3")

# Mostra as imagens
columns = st.columns(3)
for i, data in enumerate(image_data):
    with columns[i % 3]:
        img = Image.open(data["imagem"])

        # Verifica se a imagem está selecionada
        if selected_image == data["nome"]:
            img = img.highlight_factor(2)

        # Mostra a imagem e atribui a seleção ao clicar
        if st.image(img, caption=data["nome"], use_column_width=True, ):
            selected_image = data["nome"]
            translate_and_play_mp3(data["nome"])
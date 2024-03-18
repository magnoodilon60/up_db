import streamlit as st
from PIL import Image
from gtts import gTTS
import random
import time
import os

# Lista de nomes e caminhos das imagens
image_data = [
    {"nome": "Morango", "imagem": "morango.jpg"},
    {"nome": "Maçã", "imagem": "maca.jpg"},
    {"nome": "Banana", "imagem": "banana.jpg"},
    {"nome": "Abacaxi", "imagem": "abacaxi.jpg"}
]

st.title('Roleta de Frutas')

# Mostra as imagens
columns = st.columns(3)
for i, data in enumerate(image_data):
    with columns[i % 3]:
        img = Image.open(data["imagem"])
        st.image(img, caption=data["nome"], use_column_width=True)

# Botão para acionar a roleta
if st.button('Girar a roleta'):
    st.write('Girando a roleta...')
    time.sleep(3)  # Simulando o giro da roleta por 3 segundos
    chosen_fruit = random.choice(image_data)
    st.image(Image.open(chosen_fruit["imagem"]), caption=chosen_fruit["nome"], use_column_width=True)

    # Vocalização do nome da fruta em inglês
    tts = gTTS(text=chosen_fruit["nome"] + " in English is " + chosen_fruit["nome"].lower(), lang='en')
    #tts = gTTS(chosen_fruit["nome"].lower(), lang='en')
    tts.save("chosen_fruit.mp3")
    st.audio("chosen_fruit.mp3", format="audio/mp3")
    os.remove("chosen_fruit.mp3")
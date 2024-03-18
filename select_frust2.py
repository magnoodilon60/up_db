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
    {"nome": "Banana", "imagem": "banana.jpg"},
    # {"nome": "Fruta Maçã", "imagem": "maçã.jpg"},
    # {"nome": "Goiaba", "imagem": "goiaba.jpg"},
    # {"nome": "Pêra", "imagem": "pera.jpg"},
    # {"nome": "melancia", "imagem": "melancia.jpg"},
    # {"nome": "maracujá", "imagem": "maracuja.jpg"},
    # {"nome": "Manga", "imagem": "manga.jpg"},
    # {"nome": "laranja", "imagem": "laranja.jpg"},
    # {"nome": "Tomate", "imagem": "tomate.jpg"},
    # {"nome": "Acerola", "imagem": "acerola.jpg"},
    {"nome": "fruta uva", "imagem": "uva.jpg"},
]

st.title('Roleta de Frutas')

# Mostra as imagens
# columns = st.columns(3)
# for i, data in enumerate(image_data):
#     with columns[i % 3]:
#         img = Image.open(data["imagem"])
#         st.image(img, caption=data["nome"], use_column_width=True)

# Botão para acionar a roleta
if st.button('Girar a roleta'):
    st.write('Girando a roleta...')
    time.sleep(1)  # Simulando o giro da roleta por 1 segundo
    chosen_fruit = random.choice(image_data)
    translator = Translator()
    st.image(Image.open(chosen_fruit["imagem"]), caption=chosen_fruit["nome"] + '--' + translator.translate(chosen_fruit["nome"], dest='en').text, use_column_width=True)
    #st.image(Image.open(chosen_fruit["imagem"]), caption=chosen_fruit["nome"], use_column_width=True)

    # Traduzindo o nome da fruta para o inglês
    #translator = Translator()
    translated_name = translator.translate(chosen_fruit["nome"], dest='en').text

    # Vocalização do nome da fruta em inglês
    tts = gTTS(text=translated_name, lang='en')
    tts.save("chosen_fruit.mp3")
    st.audio("chosen_fruit.mp3", format="audio/mp3")
    os.remove("chosen_fruit.mp3")
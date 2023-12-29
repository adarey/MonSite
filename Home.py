import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Mon apps !",
    page_icon=":snake:",
)

imageLogo = Image.open("media/logo.png")

with st.sidebar:
    st.image(imageLogo)
    st.write("Adam Rey")

st.write("# Welcome to Streamlit! 👋")
st.write("https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/")


# Titre de l'application
st.title('Démonstration des Widgets de Streamlit')

# Widgets pour l'entrée de données
text_input = st.text_input("Entrez du texte")
number_input = st.number_input("Entrez un nombre")
text_area = st.text_area("Zone de texte")
date_input = st.date_input("Date")
time_input = st.time_input("Heure")
file_uploader = st.file_uploader("Téléchargez un fichier")

# Widgets de sélection
checkbox = st.checkbox("Cocher la case")
radio = st.radio("Choisissez une option", ['Option 1', 'Option 2', 'Option 3'])
selectbox = st.selectbox("Sélectionnez une option", ['Option A', 'Option B', 'Option C'])
multiselect = st.multiselect("Sélectionnez plusieurs options", ['Option 1', 'Option 2', 'Option 3'])

# Widgets pour l'affichage des données
slider = st.slider("Glisser pour sélectionner une valeur", 0, 100)
select_slider = st.select_slider("Glisser pour sélectionner une option", options=['Option A', 'Option B', 'Option C'])
color_picker = st.color_picker("Choisissez une couleur")

# Boutons et interactions
button = st.button("Cliquez-moi")
if button:
    st.write("Vous avez cliqué sur le bouton.")


# Widget Image

# Widget Audio
audio_file = open("media/musique.mp3", "rb") # Remplacez par le chemin de votre fichier audio
st.audio(audio_file.read(), format="audio/mp3")

# Widget Vidéo
video_file = open("media/video.mp4", "rb") # Remplacez par le chemin de votre fichier vidéo
st.video(video_file.read(), format="video/mp4")




# Affichage des informations
st.write(f"Texte entré : {text_input}")
st.write(f"Nombre entré : {number_input}")
st.write(f"Zone de texte : {text_area}")
st.write(f"Date : {date_input}")
st.write(f"Heure : {time_input}")
st.write(f"Fichier : {file_uploader}")
st.write(f"Case cochée : {checkbox}")
st.write(f"Radio sélectionné : {radio}")
st.write(f"SelectBox : {selectbox}")
st.write(f"Multiselect : {multiselect}")
st.write(f"Slider : {slider}")
st.write(f"Select Slider : {select_slider}")
st.write(f"Couleur sélectionnée : {color_picker}")

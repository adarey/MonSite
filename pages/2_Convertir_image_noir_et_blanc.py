from io import BytesIO

import streamlit as st

from PIL import Image
from rembg import remove

def convertir_image_nbw(image):
    # Convertir en noir et blanc
    image_nbw = image.convert('L')
    return image_nbw




st.title("Convertir une image")



tab1, tab2, tab3 = st.tabs(["Convertir une image en noir et blanc", "Supprimer le fond de l'image", "Je sais pas encore"])

with tab1:
    st.header("Convertir une image en noir et blanc")

    # Sélectionner une image depuis votre système de fichiers
    image = st.file_uploader("Sélectionnez une image", type=["jpg", "jpeg", "png"], key="bn")

    if image:
        # Ouvrir l'image
        image = Image.open(image)
        
        # Appeler la fonction pour la conversion en noir et blanc
        image_nbw = convertir_image_nbw(image)
        
        # Afficher l'image en noir et blanc
        st.image(image_nbw, caption="Image Noir et Blanc", use_column_width=True)

        # Convertir l'image PIL en objet BytesIO
        img_byte_arr = BytesIO()
        image_nbw.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Bouton de téléchargement
        st.download_button("Télécharger l'image", img_byte_arr, "image_nb.png", "image/png", key="dnb")







with tab2:
    st.header("Supprimer le fond de l'image")

    # Sélectionner une image depuis votre système de fichiers
    
    image_file = st.file_uploader("Sélectionnez une image", type=["jpg", "jpeg", "png"], key="sf")

    if image_file:
        # Lire le contenu du fichier dans un objet BytesIO
        image_bytes = BytesIO(image_file.read())
        image = Image.open(image_bytes)

        # Supprimer l'arrière-plan de l'image
        image_no_bg = remove(image)

        # Convertir l'image PIL en objet BytesIO pour le téléchargement
        img_byte_arr = BytesIO()
        image_no_bg.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Afficher l'image sans arrière-plan
        st.image(image_no_bg, caption="Image sans fond", use_column_width=True)

        # Bouton de téléchargement
        st.download_button("Télécharger l'image sans fond", img_byte_arr, "image_no_bg.png", "image/png")

        
        
with tab3:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

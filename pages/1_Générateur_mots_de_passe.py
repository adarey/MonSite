import streamlit as st
import random
import string
import pandas as pd

def generer_mot_de_passe(longueur, nombre):
    mots_de_passe = []
    
    for _ in range(nombre):
        mot_de_passe = ''.join(random.choices(string.ascii_letters + string.digits, k=longueur))
        mots_de_passe.append(mot_de_passe)
    
    return mots_de_passe

st.title("Générateur de Mots de Passe")

nbr_caracteres = st.number_input("Nombre de caractères pour les mots de passe :", min_value=8, step=1)
nbr_mots_de_passe = st.number_input("Nombre de mots de passe à générer :", min_value=5, step=1)

if st.button("Générer"):
    mots_de_passe_generes = generer_mot_de_passe(nbr_caracteres, nbr_mots_de_passe)
    
    # Créer un DataFrame pandas pour afficher les mots de passe dans un tableau
    data = {'Mot de passe': mots_de_passe_generes}
    df = pd.DataFrame(data)
    
    st.header("Mots de passe générés :")
    st.dataframe(df)

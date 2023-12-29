import streamlit as st
import pandas as pd

# Fonction pour calculer l'IMC
def calculer_imc(poids, taille):
    return poids / (taille ** 2)

# Fonction pour déterminer la catégorie de poids
def categorie_poids(imc):
    if imc < 18.5:
        return 'Maigre'
    elif 18.5 <= imc < 25:
        return 'Normal'
    elif 25 <= imc < 30:
        return 'En surpoids'
    else:
        return 'Obèse'

# Fonction pour calculer le poids nécessaire pour être dans la catégorie "Normal"
def poids_normal(taille):
    return 25 * (taille ** 2)

# Tableau des catégories de poids
def tableau_categories():
    categories = [
        {"Catégorie": "Maigre", "IMC": "< 18.5"},
        {"Catégorie": "Normal", "IMC": "18.5 - 24.9"},
        {"Catégorie": "En surpoids", "IMC": "25 - 29.9"},
        {"Catégorie": "Obèse", "IMC": "≥ 30"}
    ]
    return pd.DataFrame(categories)

# Titre de l'application
st.title('Calculateur d\'IMC et Catégories de Poids')

# Entrées utilisateur
poids = st.number_input('Entrez votre poids (en kg)', min_value=30, max_value=200, value=80)
taille = st.number_input('Entrez votre taille (en mètres)', min_value=1.2, max_value=2.2, value=1.83)

# Bouton de calcul
if st.button('Calculer l\'IMC et la Catégorie de Poids'):
    # Vérification des entrées
    if poids > 0 and taille > 0:
        imc = calculer_imc(poids, taille)
        categorie = categorie_poids(imc)
        st.write(f'Votre IMC est : {imc:.2f}')
        st.write(f'Catégorie de poids : {categorie}')

        # Calculer le poids normal et la perte de poids nécessaire
        if categorie != 'Normal':
            poids_ideal = poids_normal(taille)
            perte_poids_necessaire = max(poids - poids_ideal, 0)
            st.write(f'Poids idéal pour être dans la catégorie "Normal" : {poids_ideal:.2f} kg')
            st.write(f'Perte de poids nécessaire : {perte_poids_necessaire:.2f} kg')
    else:
        st.write('Veuillez entrer des valeurs valides pour le poids et la taille.')

# Affichage du tableau des catégories de poids
st.write("Tableau des Catégories de Poids en fonction de l'IMC :")
st.table(tableau_categories())

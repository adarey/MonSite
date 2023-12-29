import streamlit as st
import openai

# Remplacez 'VOTRE_CLE_API' par votre propre clé API OpenAI
openai.api_key = st.secrets["openai"]["apikey"]

st.title("Application Streamlit avec ChatGPT")

# L'utilisateur saisit un message
user_input = st.text_input("Vous voulez quoi : ", "")
if user_input:
    try:
        # Créez une liste de messages avec le message de l'utilisateur
        messages = [
            {"role": "system", "content": "Vous êtes un assistant virtuel qui peut répondre aux questions."},
            {"role": "user", "content": user_input},
        ]

        # Appelez l'API OpenAI pour obtenir une réponse
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Vous pouvez choisir le modèle de votre choix
            messages=messages,
        )

        # Récupérez la réponse du chatbot depuis la réponse de l'API
        bot_response = response['choices'][0]['message']['content']

        # Affichez la réponse du chatbot dans l'interface utilisateur
        st.text("ChatGPT : " + bot_response)
    except Exception as e:
        # En cas d'erreur, affichez un message d'erreur
        st.error(f"Une erreur s'est produite : {str(e)}")

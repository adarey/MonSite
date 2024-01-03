import streamlit as st
import sqlite3
import pandas as pd

# Création de la base de données SQLite et de la table si elle n'existe pas
conn = sqlite3.connect('liens.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS liens (categorie TEXT, nom TEXT, lien TEXT, rubrique TEXT)''')
conn.commit()

# Fonction pour afficher la liste des liens et permettre de les modifier/supprimer
def gestion_liens():
    st.header("Liste des Liens")

    # Lire les liens de la base de données
    c.execute('SELECT * FROM liens')
    rows = c.fetchall()
    df = pd.DataFrame(rows, columns=["Catégorie", "Nom", "Lien", "Rubrique"])
    
    if not df.empty:
        liens_a_modifier = st.selectbox("Sélectionnez un lien à modifier :", df['Nom'].tolist())
        
        if st.button("Supprimer le lien sélectionné"):
            try:
                c.execute('DELETE FROM liens WHERE nom = ?', (liens_a_modifier,))
                conn.commit()
                st.success("Le lien a été supprimé avec succès.")
            except Exception as e:
                st.error(f"Erreur lors de la suppression du lien : {str(e)}")
        
        nouvelle_categorie = st.text_input("Nouvelle catégorie :")
        nouveau_nom = st.text_input("Nouveau nom :")
        nouveau_lien = st.text_input("Nouveau lien :")
        nouvelle_rubrique = st.text_input("Nouvelle rubrique :")
        
        if st.button("Ajouter un lien"):
            if nouvelle_categorie and nouveau_nom and nouveau_lien and nouvelle_rubrique:
                try:
                    c.execute('INSERT INTO liens (categorie, nom, lien, rubrique) VALUES (?, ?, ?, ?)', 
                              (nouvelle_categorie, nouveau_nom, nouveau_lien, nouvelle_rubrique))
                    conn.commit()
                    st.success("Le lien a été ajouté avec succès.")
                except Exception as e:
                    st.error(f"Erreur lors de l'ajout du lien : {str(e)}")
    
    else:
        st.warning("Aucun lien n'est actuellement disponible.")

# Affichage principal
st.title("Gestionnaire de Liens")
gestion_liens()

# Afficher la liste des liens actuels sous forme de tableau
st.write("Liste des Liens Actuels :")
c.execute('SELECT * FROM liens')
rows = c.fetchall()
df = pd.DataFrame(rows, columns=["Catégorie", "Nom", "Lien", "Rubrique"])
st.dataframe(df)

conn.close()
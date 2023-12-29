import streamlit as st
import sqlite3
import pandas as pd


# Création de la base de données SQLite et de la table si elle n'existe pas
conn = sqlite3.connect('liens.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS liens (lien TEXT)''')
conn.commit()

# Fonction pour afficher la liste des liens et permettre de les modifier/supprimer
def gestion_liens():
    st.header("Liste des Liens")

    # Lire les liens de la base de données
    c.execute('SELECT * FROM liens')
    rows = c.fetchall()
    df = pd.DataFrame(rows, columns=["Liens"])
    
    if not df.empty:
        liens_a_modifier = st.selectbox("Sélectionnez un lien à modifier :", df['Liens'].tolist())
        
        if st.button("Supprimer le lien sélectionné"):
            c.execute('DELETE FROM liens WHERE lien = ?', (liens_a_modifier,))
            conn.commit()
        
        nouveau_lien = st.text_input("Nouveau lien :")
        
        if st.button("Ajouter un lien"):
            if nouveau_lien:
                c.execute('INSERT INTO liens (lien) VALUES (?)', (nouveau_lien,))
                conn.commit()
    
    else:
        st.write("Aucun lien n'est actuellement disponible.")

# Affichage principal
st.title("Gestionnaire de Liens")
gestion_liens()

# Afficher la liste des liens actuels
st.write("Liste des Liens Actuels :")
c.execute('SELECT * FROM liens')
rows = c.fetchall()
for row in rows:
    st.write(row[0])

conn.close()

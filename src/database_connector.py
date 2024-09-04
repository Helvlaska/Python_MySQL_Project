import mysql.connector

# Configuration de la connexion
config = {
    'user': 'root',
    'password': 'lnORD605303/',
    'host': '127.0.0.1',
    'database': 'DatabaseTest'
}

# Établir la connexion
conn = mysql.connector.connect(**config)

# Vérification de la connexion
if conn.is_connected():
    print("Connexion réussie à la base de données MySQL")

# Fermer la connexion
conn.close()

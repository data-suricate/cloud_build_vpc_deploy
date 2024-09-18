import os
from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Configuration de la connexion à la base de données
host = os.getenv('_HOST')
port = os.getenv('_PORT')
user = os.getenv('_USER')
password = os.getenv('_PASSWORD')
database = os.getenv('_DATABASE')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/users')
def get_users():
    print("in")
    print(" test 1")
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    # Exemple d'exécution d'une requête
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print(users)

    # Fermer la connexion
    cursor.close()
    conn.close()   
    return {"users": users}


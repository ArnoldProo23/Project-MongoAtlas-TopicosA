from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

#Cargar variables de entorno
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI_ATLAS")
DB_NAME_ATLAS = os.getenv("MONGODB_DATA")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME_ATLAS]
    print("Conexión exitosa a la base de datos.")
except errors.ConnectionFailure as e:
    print(f"Error de conexión: {e}")
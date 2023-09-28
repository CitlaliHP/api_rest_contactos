# Importamos las bibliotecas necesarias
from typing import Union
import pandas as pd
from fastapi import FastAPI
import json

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Definimos una ruta de operación GET en el servidor FastAPI
@app.get("/v1/contactos")
# Definimos una función asíncrona para manejar las solicitudes GET a la ruta "/v1/contactos"
async def read_contactos_csv():
    # Leemos el archivo CSV usando pandas
    df = pd.read_csv("contactos.csv")
    # Convertimos el DataFrame de pandas a JSON
    contactos_data = df.to_json(orient="records")
    # Devolvemos los datos en formato JSON
    return json.loads(contactos_data)

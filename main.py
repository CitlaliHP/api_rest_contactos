# Importamos las bibliotecas necesarias
from typing import Union
import pandas as pd
from fastapi import FastAPI
import json

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    """
    # Endpoint raíz de la API contactos
    ## Endpoint raíz
    """
    return 

# Definimos una ruta de operación GET en el servidor FastAPI
@app.get("/v1/contactos", status_code=202)
# Definimos una función asíncrona para manejar las solicitudes GET a la ruta "/v1/contactos"
async def read_contactos_csv():
    # Leemos el archivo CSV usando pandas
    df = pd.read_csv("contactos.csv")
    # Convertimos el DataFrame de pandas a JSON
    contactos_data = df.to_json(orient="records")
    # Devolvemos los datos en formato JSON
    return json.loads(contactos_data)

# Importa la clase FastAPI de FastAPI, así como otros módulos necesarios
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel  # Importa BaseModel de pydantic para definir modelos de datos
import csv

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define un modelo Pydantic para representar un contacto
class Contacto(BaseModel):
    nombre: str
    email: str

# Lista que almacenará los contactos
contactos_lista = []

# Ruta GET para obtener todos los contactos
@app.get("/v1/contactos", response_model=list[Contacto])
async def get_contactos():
    return contactos_lista

# Ruta POST para agregar un nuevo contacto
@app.post("/v1/contactos", response_model=Contacto, status_code=status.HTTP_201_CREATED)
async def add_contacto(contacto: Contacto):
    contactos_lista.append(contacto)
    return contacto
# Ruta GET para obtener un contacto por su índice en la lista
@app.get("/v1/contactos/{contacto_id}", response_model=Contacto)
async def get_contacto(contacto_id: int):
    # Comprueba si el índice está fuera de los límites de la lista
    if contacto_id < 0 or contacto_id >= len(contactos_lista):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no encontrado")
    return contactos_lista[contacto_id]

# Ruta GET de tu código original, que devuelve un mensaje "Hello Wold"
@app.get("/")
async def root():
    return {"message": "Hello Wold"}

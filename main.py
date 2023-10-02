# Importamos las bibliotecas necesarias
from typing import Union
import pandas as pd
from fastapi import FastAPI
import json
from pydantic import BaseModel


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

# Modelo Pydantic para representar un contacto
class Contacto(BaseModel):
    nombre: str
    email: str

# Lista que almacenará los contactos
contactos_lista = []

# Ruta GET para obtener todos los contactos y mostrar el contenido del archivo CSV
@app.get("/v1/contactos", response_model=list[Contacto])
async def get_contactos():
    # Lee el contenido del archivo CSV
    try:
        with open("contactos.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            contactos_lista = [{"nombre": row["nombre"], "email": row["email"]} for row in reader]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="El archivo 'contactos.csv' no se encontró")

    return contactos_lista

# Ruta POST para agregar un nuevo contacto
@app.post("/v1/contactos", response_model=Contacto)
async def add_contacto(contacto: Contacto):
    contactos_lista.append(contacto)
    return contacto

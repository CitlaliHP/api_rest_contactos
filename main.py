# Importamos las bibliotecas necesarias
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

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
@app.post("/v1/contactoss", response_model=Contacto)
async def add_contacto(contacto: Contacto):
    # Agrega el nuevo contacto a la lista
    contactos_lista.append({"nombre": contacto.nombre, "email": contacto.email})
    
    # Escribe la lista de contactos en el archivo CSV
    try:
        with open("contactos.csv", mode="a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["nombre", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()  # Escribe la cabecera solo si el archivo está vacío
            writer.writerow({"nombre": contacto.nombre, "email": contacto.email})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar el contacto: {str(e)}")
    
    return contacto

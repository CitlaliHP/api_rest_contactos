# Importamos las bibliotecas necesarias
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Modelo Pydantic para representar un contacto
class Contacto(BaseModel):
    id: int
    nombre: str
    primerApellido: str
    segundoApellido: str
    email: str
    telefono: str

# Lista que almacenará los contactos
contactos_lista = []

# Ruta GET para obtener todos los contactos y mostrar el contenido del archivo CSV
@app.get("/v2/contactos", response_model=list[Contacto])
async def get_contacto():
    # Lee el contenido del archivo CSV
    try:
        with open("contacto.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            contactos_lista = [{"id": row["id"], "nombre": row["nombre"], "primerApellido": row["primerApellido"], "segundoApellido": row["segundoApellido"], "email": row["email"], "telefono": row["telefono"]} for row in reader]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="El archivo 'contactos.csv' no se encontró")

    return contactos_lista

# Ruta POST para agregar un nuevo contacto
@app.post("/v2/contactos", response_model=Contacto)
async def add_contacto(contacto: Contacto):
    # Agrega el nuevo contacto a la lista
    contactos_lista.append({"id": contacto.id, "nombre": contacto.nombre,"primerApellido": contacto.primerApellido, "segundoApellido": contacto.segundoApellido, "email": contacto.email, "telefono": contacto.telefono})
    
    # Escribe la lista de contactos en el archivo CSV
    try:
        
        with open("contacto.csv", mode="a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "nombre","primerApellido", "segundoApellido", "email", "telefono"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()  # Escribe la cabecera solo si el archivo está vacío
            writer.writerow({"id": contacto.id, "nombre": contacto.nombre,"primerApellido": contacto.primerApellido, "segundoApellido": contacto.segundoApellido, "email": contacto.email, "telefono": contacto.telefono})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar el contacto: {str(e)}")
    
    return contacto

# Ruta PUT/PATCH para actualizar los datos de un contacto
@app.put("/contactos/{id}", response_model=Contacto)
async def update_contacto(id: int, contacto: Contacto):
    # Busca el contacto por id_contacto y actualiza sus datos
    for i in range(len(contactos_lista)):
        if contactos_lista[i]['id'] == id:
            contactos_lista[i] = {"id": contacto.id, "nombre": contacto.nombre,"primerApellido": contacto.primerApellido, "segundoApellido": contacto.segundoApellido, "email": contacto.email, "telefono": contacto.telefono}
            break
    else:
        raise HTTPException(status_code=404, detail=f"El contacto con id {id} no se encontró")

    # Actualiza el archivo CSV con los nuevos datos del contacto
    try:
        with open("contacto.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "nombre","primerApellido", "segundoApellido", "email", "telefono"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for c in contactos_lista:
                writer.writerow(c)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el contacto: {str(e)}")

    return {"id": contacto.id, "nombre": contacto.nombre,"primerApellido": contacto.primerApellido, "segundoApellido": contacto.segundoApellido, "email": contacto.email, "telefono": contacto.telefono}

# Ruta DELETE para borrar un contacto
@app.delete("/contactos/{id}")
async def delete_contacto(id: int):
    # Busca el contacto por id_contacto y lo borra de la lista de contactos y del archivo CSV
    for i in range(len(contactos_lista)):
        if contactos_lista[i]['id'] == id:
            del contactos_lista[i]
            break
    else:
        raise HTTPException(status_code=404, detail=f"El contacto con id {id_contacto} no se encontró")

    # Actualiza el archivo CSV después de borrar el contacto
    try:
        with open("contacto.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "nombre","primerApellido", "segundoApellido", "email", "telefono"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for c in contactos_lista:
                writer.writerow(c)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al borrar el contacto: {str(e)}")

    return {"detail": f"El contacto con id {id_contacto} ha sido borrado"}

# Ruta GET para buscar contactos por nombre
@app.get("/contactos/{nombre}", response_model=list[Contacto])
async def search_contactos(nombre: str):
    # Busca contactos que contengan el nombre buscado en la lista de contactos
    contactos_filtrados = [c for c in contactos_lista if nombre.lower() in c['nombre'].lower()]

    return contactos_filtrados

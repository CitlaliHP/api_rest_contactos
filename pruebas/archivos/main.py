import os
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

# Rutas de destino para PDFs e imágenes
pdf_path = "pruebas/archivos/static/pdf/"
image_path = "pruebas/archivos/static/imagenes/"

@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")]
):
    for file in files:
        # Verificar la extensión del archivo
        if file.filename.endswith(".pdf"):
            destination = os.path.join(pdf_path, file.filename)
        elif file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            destination = os.path.join(image_path, file.filename)
        else:
            return {"error": "Formato de archivo no válido"}

        # Guardar el archivo en la ruta correspondiente
        with open(destination, "wb") as file_object:
            file_object.write(file.file.read())
    
    return {"message": "Archivo(s) subido(s) exitosamente"}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)

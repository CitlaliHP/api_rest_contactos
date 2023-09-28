from typing import Union

from fastapi import FastAPI

from asposecells.api import Workbook

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/v1/contactos")
def read_root():
    return {"Hello": "World"}

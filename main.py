from typing import Union
import csv
from fastapi import FastAPI
from asposecells.api import Workbook

import jpype
jpype.startJVM()

workbook = Workbook("contactos.csv")
workbook.save("contactos.json")

jpype.shutdownJVM()

app = FastAPI()

@app.get("/v1/contactos")
def read_root():
    return {"Hello": "World"}

# Define a function to read the CSV file and return its data as JSON
def read_contactos_csv():
    response = []
    with open("contactos.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            response.append(row)
    return response

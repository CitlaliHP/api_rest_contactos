from typing import Union
import pandas as pd
from fastapi import FastAPI
import json

app = FastAPI()

# Define a function to read the CSV file and return its data as JSON
@app.get("/v1/contactos")
async def read_contactos_csv():
    df = pd.read_csv("contactos.csv")
    contactos_data = df.to_json(orient="records")
    return json.loads(contactos_data)

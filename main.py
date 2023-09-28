from typing import Union
import csv
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/contactos")
def read_root():
    return {"Hello": "World"}

# Define a function to read the CSV file and return its data as JSON
@app.get("/v1/contactos_csv")
def read_contactos_csv():
    df = pd.read_csv("contactos.csv")
    return df.to_dict(orient='records')

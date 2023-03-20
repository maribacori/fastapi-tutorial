from typing import Union

from fastapi import FastAPI, Header

from pydantic import BaseModel

app = FastAPI()

banco_de_dados = []

class MapaAstral(BaseModel):
    full_name: str | None = None
    year: int
    month: int
    day: int
    hour: float
    minuts: float
    city: str
    nation: str

@app.post("/user")
def add_mapa_astral(novo_mapa: MapaAstral):
    banco_de_dados.append(novo_mapa)
    return novo_mapa

@app.get("/user")
def list_user():
    return banco_de_dados


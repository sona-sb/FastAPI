import os
from fastapi import FastAPI
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel
import requests

app = FastAPI() 

class Text(BaseModel):
    text:str
class Parts(BaseModel):
    parts:List[Text]
class Contents(BaseModel):
    contents:List[Parts]


@app.get("/{id}")
def read_root(id:int):
    return {"Hello": f'World{id}'}

@app.get("/")
def read_root(condition: int ):
    if condition==1:
        return {"Hello": "World"}
    elif condition==2:
        return {"welcome":"world"}
    else:
        return {"bye":"world"}


load_dotenv()
gemini_api= os.getenv("gemini")

@app.post("/generate")
def generate(content:Contents):
    response=requests.post(url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api}",json=content.model_dump())
    response_body=response.json()
    return response_body["candidates"][0]["content"]["parts"][0]["text"]


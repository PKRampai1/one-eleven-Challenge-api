from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    data: str
 

@app.get("/data")
def create_item(item: Item):

    a = list(item.data)
    a.sort()

    return {"word": a}
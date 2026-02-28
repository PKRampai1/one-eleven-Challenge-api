from fastapi import FastAPI ,Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    data: str
 

@app.post("/data")
async def webhook(request: Request):
    data = await request.body()
    word = data.decode("utf-8")
    a = list(word)
    a.sort()
    return {"word": a}
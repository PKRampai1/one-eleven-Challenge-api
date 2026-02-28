from fastapi import FastAPI ,Request
from pydantic import BaseModel
import re
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}



@app.post("/data")
async def webhook(request: Request):
    data = await request.body()
    word = data.decode("utf-8")
    parsed = json.loads(word)
    s2 = re.sub(r'[^a-zA-Z0-9]', '', parsed["data"])
  
    a = list(s2)
    a.sort()
    a = [f'{char}' for char in a]
    return {"word": a}
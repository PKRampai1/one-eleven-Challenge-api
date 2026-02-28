from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/data")
def create_item(data: str):
    a = list(data)
    a.sort()

    return {"word": a}
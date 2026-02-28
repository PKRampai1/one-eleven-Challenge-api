from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/words")
def create_item(word: str):
    a = list(word)
    a.sort()

    return a
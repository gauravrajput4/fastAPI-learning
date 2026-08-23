from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Akhil..!"}

@app.get("/add")
def add(a:int, b:int):
    return a+b
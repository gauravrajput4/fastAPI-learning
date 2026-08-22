from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class Response(BaseModel):
    name: str
    age: int

@app.get("/")
def root():
    return {"message":"Welcome to my app"}

@app.get("/users",response_model=Response)
def get_users():
    return {
        "name": "Akhil",
        "age": 18,
        "password": "whfsauifgawvluxo3872e"
    }

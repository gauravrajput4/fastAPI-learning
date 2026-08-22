from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.get('/')
def home():
    return {'message': 'Welcome to FastAPI with Pydantic Model'}

@app.post('/create-user')
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post('/user')
def signup(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
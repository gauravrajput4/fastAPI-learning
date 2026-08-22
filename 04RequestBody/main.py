from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.get('/')
def home():
    return {"message": "FastAPI" }

@app.post('/signup')
def signup(user:User):
    return {
        'message': 'Signup successful',
        'user': user
    }

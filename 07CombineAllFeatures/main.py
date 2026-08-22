from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users=[]

class User(BaseModel):
    name:str
    age:int

@app.get("/")
async def root():
    return {"message":"Welcome to my app"}

@app.post('/users')
def create_user(user: User):
    users.append(user)
    return {
        "message":"User Created",
        "data":user
    }

@app.put("/users/{userid}")
def update_user(userid: int, user: User,notify:bool=False):
    if userid<len(users):
        users[userid]=user
        return {
            "message":"User Updated",
            "data":user,
            "notify":notify
        }
    return {
        "message":"User not found",
    }


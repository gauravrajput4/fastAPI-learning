from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to my app"}

@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message":"User Created"}

@app.get("/user")
def get_users():
    return {
        "status": "success",
        "message": "User fetch",
         "data":{
             "name" :"Akhil",
             "age":22
         }
    }

@app.get("/users/{userid}")
def get_user(userid:int):
    if userid!=1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found"
        )
    return {
        "id": userid,
        "status": "success",
        "message": "User fetch"

    }
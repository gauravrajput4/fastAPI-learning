from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@app.get("/user/{userId}")
def user(userId:int):
    return {"message":f"User id of the user is {userId}"}
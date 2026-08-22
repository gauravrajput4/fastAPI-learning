from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse


app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found"
        },
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name != "Akhil":
        raise UserNotFoundException(name)
    return {"name": name}
@app.get("/users/{userid}")
def get_user(userid: int):
    if userid != 1:
        raise HTTPException(
            status_code=404,
            detail=f"User {userid} not found",
        )
    return {
        "id": userid,
        "status": "success",
        "name": "Akhil"
    }
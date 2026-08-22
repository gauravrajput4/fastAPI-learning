from fastapi import FastAPI,Depends,Header, HTTPException


app = FastAPI()

def common_logic():
    return {
        "message":"Common logic executed"
    }

@app.get("/home")
def home(data=Depends(common_logic)):
    return data


def get_current_user():
    return {
        "user":"Guest"
    }

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user=Depends(get_current_user)):
    return user


def verify_token(token:str=Header(None)):
    if token is None:
        raise HTTPException(status_code=401,
                            detail="Invalid token")
    if token!="mysecrettoken":
        raise HTTPException(status_code=401,
                            detail="unauthorized token")
    return {
        "user":"Authorized user"
    }

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return {
        "message":"Secure data accessed",
        "user":user

    }
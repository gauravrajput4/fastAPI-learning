from fastapi import FastAPI, HTTPException,Depends,Header
from jose import jwt
from datetime import datetime,timedelta,timezone

app = FastAPI()

SECRET_KEY="my-super-secret"

ALGORITHM = "HS256"

# Create Token
def create_token(data:dict):
    to_encode=data.copy()
    expire= datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update(
        {
            "exp": expire
        }
    )

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

#Login API (Token Generate)
@app.post("/login")
def login(username:str,password:str):
    if username=="" or password=="":
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    if username!="admin" or password!="admin123":
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    token=create_token(
        {
            "sub":username
        }
    )

    return {
        "access_token":token
    }

# Token Verify
def verify_token(token:str=Header(None)):

    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

# Protected Routes
@app.get("/secure")
def secure_data(user=Depends(verify_token)):
    return {
        "message":"Secure data",
        "user":user
    }


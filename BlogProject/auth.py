from jose import jwt,JWTError
from datetime import datetime, timedelta,timezone
from fastapi import HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY="mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_schema= OAuth2PasswordBearer(tokenUrl="/login")

# create token
def create_token(data:dict):
    to_encode=data.copy()

    expires=datetime.now(timezone.utc)+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expires})

    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

# verify token
def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expire token")
from fastapi import FastAPI,HTTPException,Depends
from jose import jwt,JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext


app = FastAPI()

# jwt config
SECRET_KEY = "my-super-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Password Hashing Setup
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth setup
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

# Dummy user DB
fake_user={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

# Hash Password
def hashed_password(password:str):
    return pwd_context.hash(password)

# verify Password
def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

#create Token
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

# Login API (OAuth2 Form)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = fake_user.get(form_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=404, detail="Incorrect password")
    access_token=create_token(
        {
            "sub":form_data.username,
            "message":"successfully logged in",
        }
    )

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

# Verify Token
def verify_token(token:str=Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        if not username:
            raise HTTPException(status_code=404, detail="Incorrect username")
        return username
    except JWTError:
        raise HTTPException(status_code=404, detail="Incorrect token")


# Protect Routes..
@app.get("/protected")
def protected_route(username:str=Depends(verify_token)):
    return {
        "message":f"Hello, you have to access to this protected route!",
        "user":username
    }



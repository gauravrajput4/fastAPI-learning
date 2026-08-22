from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return "welcome to FastAPI"

# Optional
@app.get('/users')
def get_users(name: str= None):
    return {"name":name}

# Default Value
@app.get('/product')
def product(limit:int=100):
    return {"limit":limit}

# Multiple Query Parameters
@app.get('/items')
def items(name:str=None, price:int=0):
    return {"name":name, "price":price}

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Address(BaseModel):
    city:str
    pincode:int
    state:str
class UserCreate(BaseModel):
    id:int
    name: str
    city: str
    address: Address
    occupation:str
@app.get("/")
def home():
    return {"message":"CRUD operation in FastAPI"}

usersData=[]

@app.get('/all-users')
def all_users():
    return {
        "message":"All users data",
        "data":usersData
    }

@app.post('/create-user')
def create_user(user: UserCreate):
    data =user.dict()
    usersData.append(data)
    return {
        "message":"User created successfully",
        "data":data
    }

@app.delete('/delete-user/{id}')
def delete_user(id: int):
    for user in usersData:
        if user['id'] == id:
            usersData.remove(user)
            return {
                "message":"User deleted successfully"
            }
    return {
        "message":"user Not found"
    }

@app.patch('/update-user/{id}')
def update_user(id: int, data: UserCreate):
    for user in usersData:
        print(user)
        print(user['id'])
        if user['id'] == id:
            user['name'] = data.name
            user['city'] = data.city
            user['address'] = data.address
            user['occupation'] = data.occupation
            return {
                "message":"User updated successfully",
                "data":data
            }
    return {
        "message":"user Not found"
    }

@app.put('/users/{id}')
def update_user(id: int, data: UserCreate):
    for index,user in enumerate(usersData):
        if user.id == id:
            user[index] = data
            return {
                "message":"User updated successfully",
                "data":data
            }
    return {
        "message":"user Not found"
    }


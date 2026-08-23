# import requests
#
# response =requests.get("https://jsonplaceholder.typicode.com/posts")
#
# data = response.json()
# print(data[:2])

from fastapi import FastAPI
import requests

app = FastAPI()

# Get all data
@app.get("/post")
def get_post():
    url="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    return response.json()

@app.get("/post/{id}")
def get_post(id: int):
    url=f"https://jsonplaceholder.typicode.com/posts/{id}"
    response=requests.get(url)
    return response.json()
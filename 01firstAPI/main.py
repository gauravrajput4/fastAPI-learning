from fastapi import FastAPI

app = FastAPI()

# HOME Route
@app.get("/")
def home():
    return {'message':'Welcome to FastAPI!'}

@app.get('/about')
def about():
    return {'message':'This is about page'}

@app.get('/users')
def users():
    return {
        'user':[
            {
                'name':'Gaurav',
                'city':'Kannauj'
            },
            {
                'name':'Akhil',
                'city':'Kanpur'
            }
        ]
    }
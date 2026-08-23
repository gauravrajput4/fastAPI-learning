from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed Origins( Frontend URL)
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allowed Frontend
    allow_credentials=True,
    allow_methods=["*"], # GET, PUT,POST,DELETE
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "CORS Enable API"}
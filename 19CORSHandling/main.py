from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
# from dotenv import load_dotenv
# import os
# load_dotenv()

app = FastAPI()

# Allowed Origins( Frontend URL)
# origins = os.getenv("ORIGINS")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins, # Allowed Frontend
    allow_credentials=True,
    allow_methods=["*"], # GET, PUT,POST,DELETE
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "CORS Enable API"}
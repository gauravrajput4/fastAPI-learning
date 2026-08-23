from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Step 1: Ensure Upload folder exists
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Step 2: Static file set-up
# URL: http://127.0.0.1:8080/files/<file_name>
app.mount("/files",StaticFiles(directory=UPLOAD_FOLDER),name="files")

#Step 3: Upload file API
@app.post("/upload")
def upload_file(file:UploadFile=File(...)):
    file_name=file.filename
    file_path=os.path.join(UPLOAD_FOLDER,file_name)

    if not file_name:
        raise HTTPException(
            status_code=400,
            detail="File Not select"
        )
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

        return {
            "statusCode": 200,
            "message":"File uploaded successfully",
            "fileName":file_name,
            "file_url":f"http://127.0.0.1:8000/files/{file_name}"
        }

# Step 4: Get File URL API
@app.get("/files/{file_name}")
def get_file(file_name:str):
    file_path=os.path.join(UPLOAD_FOLDER,file_name)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=400,
            detail="File Not exists"
        )

    return {
        "file_url": f"http://127.0.0.1:8000/files/{file_name}"
    }

@app.get("/")
def home():
    return {
        "statusCode": 200,
        "message": "Welcome to FastAPI!",
    }

import shutil

from fastapi import FastAPI,UploadFile
from
import uuid
from

app = FastAPI(titl= "UploadFile", docs_url='/')
@app.post('/')
def upload_file(file: UploadFile):
    image_upload(file)
    return {"message": "Uploaded successfully"}
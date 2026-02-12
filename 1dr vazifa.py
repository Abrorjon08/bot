import datetime

from fastapi import FastAPI, UploadFile

app = FastAPI(docs_url="/", title="Vazifa")

@app.post("/file_upload")
def file_yuklash (file: UploadFile):
    yuklash = ("jpg", "jpeg", "png", "gif", "webp")
    hajmi = 2*1024*1024 # 2
    if not file.filename.lower().endswith(yuklash):
        return {"message": "File formati rasim emas ⁉️"}
    if file.size > hajmi:
        return {"message": "File hajim oshib ketdi 2 mb dan"}
    return {
        "filename": file.filename,
        "hajmi": file.size,
        "yuklash vaqti": datetime.datetime.now(),
        "fayl turi ": file.content_type
    }
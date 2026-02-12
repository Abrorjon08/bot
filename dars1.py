from fastapi import File, UploadFile
import shutil
import uuid

def file_yuklash(file: UploadFile):
    rasm_formatlari = ('jpg', 'jpeg', 'png', 'svg', 'jfif')
    if not file.filename.lower().endswith(rasm_formatlari):
      return {'message': 'File formati rasm emas !!!'}

    hajm = 4 * 1024 * 1024  # 2 mb
    if file.size > hajm:
      return {'message': 'File hajmi oshib ketdi ( 2mb )'}
    with open(f"files/{uuid.uuid4()}", 'wb') as rasm:
      shutil.copyfileobj(file.file, rasm)
    return {"masg" :"File upload⁉️"}



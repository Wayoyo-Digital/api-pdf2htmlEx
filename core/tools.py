import os

from fastapi import File, UploadFile

UPLOAD_PATH = os.path.abspath(f"storage/uploads")

def sanitize_filename(filename):
    return filename.replace(" ", "-")


async def upload_temp_file(file: UploadFile = File(...)):
    filename = file.filename or "default.pdf"
    save_path = os.path.join(UPLOAD_PATH, sanitize_filename(filename))
    
    with open(save_path, "wb") as f:
        f.write(await file.read())
    
    return save_path
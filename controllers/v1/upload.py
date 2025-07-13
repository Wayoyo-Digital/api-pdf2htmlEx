from fastapi import APIRouter, UploadFile, File

from core.tools import UPLOAD_PATH, upload_temp_file
from services.commands.bus import Bus as Command 

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = await upload_temp_file(file)
    Command.get_instance().execute('pdf2htmlex', save_path, f'--dest-dir={UPLOAD_PATH}')
    
    return {"filename": file.filename, "save_path": save_path}

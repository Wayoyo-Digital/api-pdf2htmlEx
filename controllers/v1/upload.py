from fastapi import APIRouter, UploadFile, File

from core.tools import PDF2HTML_PATH, UPLOAD_PATH, upload_temp_file
from services.commands.bus import Bus as Command 

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = await upload_temp_file(file)
    Command.get_instance().execute(
        'pdf2htmlex',
        f'--data-dir={PDF2HTML_PATH}',
        f'--process-outline=0',
        f'--dest-dir={UPLOAD_PATH}',
        save_path
    )
    
    return {"filename": file.filename, "save_path": save_path}

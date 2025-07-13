import os
import pathlib
from typing import Optional
from starlette.status import HTTP_400_BAD_REQUEST

from fastapi import File, UploadFile, HTTPException

PDF2HTML_PATH = os.path.abspath("core/pdf2htmlEX")
UPLOAD_PATH = os.path.abspath("storage/uploads")

def sanitize_filename(filename: str, default_ext: Optional[str] = ".pdf") -> str:
    """
    Sanitize filename to prevent directory traversal while preserving file extension.
    If no extension is present, adds default_ext (default: .pdf). If default_ext is None, does not add any extension.
    """
    name, ext = os.path.splitext(os.path.basename(filename))
    name = "".join(char for char in name if ord(char) >= 32)
    ext = "".join(char for char in ext if ord(char) >= 32)
    for char in ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', ' ', '.']:
        name = name.replace(char, '_')
    if ext:
        ext = '.' + ext.lstrip('.').replace('.', '_')
    if not name:
        name = 'unnamed_file'
    if not ext and default_ext:
        ext = default_ext
    return name + ext

def ensure_upload_dir() -> None:
    """
    Ensure the upload directory exists and has proper permissions.
    """
    pathlib.Path(UPLOAD_PATH).mkdir(parents=True, exist_ok=True)
    os.chmod(UPLOAD_PATH, 0o700)

async def upload_temp_file(file: UploadFile = File(...)) -> str:
    """
    Safely upload a temporary file to the upload directory.
    """
    if not file.filename:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No filename provided")
    
    ensure_upload_dir()
    
    safe_filename = sanitize_filename(file.filename)
    save_path = os.path.join(UPLOAD_PATH, safe_filename)
    
    if not os.path.abspath(save_path).startswith(os.path.abspath(UPLOAD_PATH)):
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid file path")
    
    with open(save_path, "wb") as f:
        while chunk := await file.read(8192):  # 8KB chunks
            f.write(chunk)

    return save_path
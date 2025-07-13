from fastapi import APIRouter
from fastapi.responses import FileResponse

from core.tools import UPLOAD_PATH, sanitize_filename

router = APIRouter()

@router.get("/html/{filename}")
async def get_html(filename: str):
    import os
    from fastapi import HTTPException
    from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

    # Strip extension before sanitizing, and do not add any default extension
    name_only = os.path.splitext(filename)[0]
    safe_name = sanitize_filename(name_only, default_ext=".html")
    html_path = os.path.join(UPLOAD_PATH, safe_name)

    # Ensure the final path is still within UPLOAD_PATH (defense in depth)
    if not os.path.abspath(html_path).startswith(os.path.abspath(UPLOAD_PATH)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Invalid file path"
        )

    if not os.path.isfile(html_path):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"The HTML file '{safe_name}.html' does not exist."
        )
    return FileResponse(html_path)
from fastapi import APIRouter
from fastapi.responses import FileResponse

from core.tools import UPLOAD_PATH, sanitize_filename

router = APIRouter()

@router.get("/html/{filename}")
async def get_html(filename: str):
    import os
    from fastapi import HTTPException
    from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

    # Sanitize the filename (preserve .html extension)
    safe_filename = sanitize_filename(filename)
    html_path = os.path.join(UPLOAD_PATH, f"{safe_filename}.html")

    # Ensure the final path is still within UPLOAD_PATH (defense in depth)
    if not os.path.abspath(html_path).startswith(os.path.abspath(UPLOAD_PATH)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Invalid file path"
        )

    if not os.path.isfile(html_path):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"The HTML file '{safe_filename}.html' does not exist."
        )
    return FileResponse(html_path)
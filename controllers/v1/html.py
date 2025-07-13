from fastapi import APIRouter
from fastapi.responses import FileResponse

from core.tools import UPLOAD_PATH

router = APIRouter()

@router.get("/html/{filename}")
async def get_html(filename: str):
    import os
    from fastapi import HTTPException
    from starlette.status import HTTP_404_NOT_FOUND

    html_path = os.path.join(UPLOAD_PATH, f"{filename}.html")
    if not os.path.isfile(html_path):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"The HTML file '{filename}.html' does not exist."
        )
    return FileResponse(html_path)
from typing import Union
from fastapi import APIRouter

router = APIRouter()

@router.get("/sample/{item_id}")
def sample(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

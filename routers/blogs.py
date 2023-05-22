from typing import Optional

from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(prefix='/blogs', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@router.get("/", status_code=status.HTTP_200_OK)
async def list_blogs():
    return {"message": "List of blogs"}


@router.get("/{pk}", status_code=status.HTTP_200_OK)
async def show_blog(pk: int, response: Response):
    if pk > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"data": "Not Found"}
    else:
        return {"message": f"Blog with id {pk}"}


@router.post("/")
async def create_post(data: BlogModel):
    return "ok"

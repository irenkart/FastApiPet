from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from db.db_post import create, update, retrieve, get_list, delete
from scemas import PostPatch, PostBase, PostDisplay

router = APIRouter(prefix='/posts', tags=['post'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostDisplay)
async def create_post(request: PostBase, db: Session = Depends(get_db)):
    new_user = await create(db, request)
    return new_user


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PostDisplay])
async def get_posts_list(db: Session = Depends(get_db)):
    return await get_list(db)


@router.get("/{pk}", status_code=status.HTTP_200_OK, response_model=PostDisplay)
async def retrieve_post(pk: int, db: Session = Depends(get_db)):
    return await retrieve(db, pk)


@router.patch("/{pk}", status_code=status.HTTP_200_OK, response_model=PostDisplay)
async def patch_post(pk: int, request: PostPatch, db: Session = Depends(get_db)):
    return await update(db, pk, request, partial=True)


@router.put("/{pk}", status_code=status.HTTP_200_OK, response_model=PostDisplay)
async def put_post(pk: int, request: PostBase, db: Session = Depends(get_db)):
    return await update(db, pk, request, partial=False)


@router.delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(pk: int, db: Session = Depends(get_db)):
    await delete(db, pk)
    return {}

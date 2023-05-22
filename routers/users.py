from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from db.db_user import create_user, get_users, get_user_by_id, update_user, delete_user
from scemas import UserBase, UserDisplay, UserPatch

router = APIRouter(prefix='/accounts', tags=['user'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserDisplay)
async def create_account(request: UserBase, db: Session = Depends(get_db)):
    new_user = await create_user(db, request)
    return new_user


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserDisplay])
async def list_accounts(db: Session = Depends(get_db)):
    return await get_users(db)


@router.get("/{pk}", status_code=status.HTTP_200_OK, response_model=UserDisplay)
async def retrieve_account(pk: int, db: Session = Depends(get_db)):
    return await get_user_by_id(db, pk)


@router.patch("/{pk}", status_code=status.HTTP_200_OK, response_model=UserDisplay)
async def patch_account(pk: int, request: UserPatch, db: Session = Depends(get_db)):
    return await update_user(db, pk, request, partial=True)


@router.put("/{pk}", status_code=status.HTTP_200_OK, response_model=UserDisplay)
async def put_account(pk: int, request: UserBase, db: Session = Depends(get_db)):
    return await update_user(db, pk, request, partial=False)


@router.delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(pk: int, db: Session = Depends(get_db)):
    await delete_user(db, pk)
    return {}

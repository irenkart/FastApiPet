from typing import Union

from sqlalchemy.orm import Session

from db.models import DbUser
from scemas import UserBase, UserPatch
from db.hash import Hash


async def create_user(db: Session, user_data: UserBase) -> DbUser:
    new_user = DbUser(
        username=user_data.username,
        email=user_data.email,
        password=await Hash.bcrypt(user_data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_user_by_id(db: Session, user_id: int) -> DbUser:
    return db.query(DbUser).filter(DbUser.id == user_id).first()


async def get_users(db: Session):
    return db.query(DbUser).all()


async def update_user(db: Session, user_id: int, user_data: Union[UserPatch, UserBase], partial: bool = True) -> DbUser:
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if partial:
        update_data = user_data.dict(exclude_unset=True)
        if 'password' in update_data:
            update_data['password'] = await Hash.bcrypt(update_data['password'])
    else:
        update_data = user_data.dict()
        update_data['password'] = await Hash.bcrypt(update_data['password'])
    user.update(update_data)
    db.commit()
    return user.first()


async def delete_user(db: Session, user_id: int) -> None:
    user = db.query(DbUser).filter(DbUser.id == user_id)
    user.delete()
    db.commit()

from typing import Union

from sqlalchemy.orm import Session

from db.models import DbPost
from scemas import PostBase, PostPatch


async def create(db: Session, post_data: PostBase) -> DbPost:
    new_post = DbPost(
        title=post_data.title,
        body=post_data.body,
        user_id=post_data.user_id,
        published=post_data.published
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


async def retrieve(db: Session, pk: int) -> DbPost:
    return db.query(DbPost).filter(DbPost.id == pk).first()


async def get_list(db: Session):
    return db.query(DbPost).all()


async def update(db: Session, pk: int, data: Union[PostBase, PostPatch], partial: bool = True) -> DbPost:
    post = db.query(DbPost).filter(DbPost.id == pk)
    if partial:
        update_data = data.dict(exclude_unset=True)
    else:
        update_data = data.dict()
    post.update(update_data)
    db.commit()
    return post.first()


async def delete(db: Session, pk: int) -> None:
    user = db.query(DbPost).filter(DbPost.id == pk)
    user.delete()
    db.commit()

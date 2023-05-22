from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    """Post schema displaying in User info"""
    id: int
    title: str
    body: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserPatch(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]


class UserDisplay(BaseModel):
    username: str
    email: str
    id: int
    posts: list[Post] = []

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    body: str
    published: bool = False
    user_id: int


class PostPatch(BaseModel):
    title: Optional[str]
    body: Optional[str]
    published: Optional[bool] = None


class User(BaseModel):
    """User schema displaying in Post info"""
    username: str
    email: str
    id: int

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    title: str
    body: str
    published: bool = False
    user: User
    id: int

    class Config:
        orm_mode = True

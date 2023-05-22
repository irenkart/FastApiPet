from fastapi import FastAPI

from db import models
from db.database import engine
from routers import blogs, users, posts

app = FastAPI()
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(posts.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(bind=engine)

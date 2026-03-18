from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB import Post, get_async_session, init_db
from src.schema import Post, PostResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session),
):
    post = post(
        caption=caption, url="dummyurl", file_type="photo", file_name="dummy name"
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed"):
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).oreder_by(Post.created_at.desc()))
    post = [row[0] for row in result.all()]

    post_data = []
    for post in posts:
        post_data.append({
            "id":str(post.id),
            "caption":post.caption,
            "url":post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at
        })
    return {"posts": post_data}

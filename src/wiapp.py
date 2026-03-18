from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB import Post, get_async_session, init_db
from src.schema import Post, PostResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


# define methods
@app.get("/posts ")
def get_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get(f"/posts/{id}")
def get_single_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="no such post/directory")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: Post) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}

    text_posts[max(text_posts.keys()) + 1] = {
        "title": post.title,
        "content": post.content,
    }
    return new_post

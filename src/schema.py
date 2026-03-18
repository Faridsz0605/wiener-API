from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    title: str
    content: str

from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {1: {"hello": "world", "content": "example"}}


# define methods
@app.get("/posts ")
def get_posts():
    return text_posts


@app.get(f"/posts/{id}")
def get_single_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="no such post/directory")
    return text_posts.get(id)

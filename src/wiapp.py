from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {"hello": "world", "content": "example"},
    2: {"hello": "universe", "content": "exploration"},
    3: {"hello": "dev", "content": "debugging"},
    4: {"hello": "user", "content": "profile_data"},
    5: {"hello": "client", "content": "request_payload"},
    6: {"hello": "server", "content": "response_status"},
    7: {"hello": "cloud", "content": "deployment"},
    8: {"hello": "coder", "content": "syntax_highlight"},
    9: {"hello": "tester", "content": "unit_tests"},
    10: {"hello": "admin", "content": "dashboard_stats"},
}


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

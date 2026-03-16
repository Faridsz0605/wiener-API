from fastapi import FastAPI

app = FastAPI()


# define methods
@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}

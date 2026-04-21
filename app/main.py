from fastapi import FastAPI

app = FastAPI(
    title="Feelings Clasifier"
)

@app.router.get("/")
def hello_world():
    return "Hello world"
from fastapi import FastAPI
from asgi2wsgi import asgi2wsgi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app = asgi2wsgi(app)

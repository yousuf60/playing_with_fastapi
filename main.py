from fastapi import FastAPI
from pages import cats
from pages import birds

app = FastAPI()
app.include_router(cats.root)
app.include_router(birds.root)


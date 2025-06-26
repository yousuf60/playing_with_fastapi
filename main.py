from fastapi import FastAPI
import fastapi
from pages import main_html
from pages import cats
from pages import birds

app = FastAPI()
app.include_router(cats.root)
app.include_router(birds.root)

@app.get("/")
async def supermain()->fastapi.responses.HTMLResponse:
    return main_html


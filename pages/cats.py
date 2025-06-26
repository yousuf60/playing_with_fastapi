from fastapi import APIRouter

from .shared import *


root_html = link_list(
    [
        ("home","home cats"),
    ]
)

root = APIRouter(prefix="/cats")

@root.get("/")
async def tempmain() -> HTMLResponse:
    return root_html

@root.get("/home")
async def homy() -> HTMLResponse:
    return HTMLResponse("mewmew")


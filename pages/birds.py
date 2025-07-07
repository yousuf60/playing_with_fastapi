from fastapi import APIRouter
from .shared import *

root_html = link_list(
    [
        ("owl","owl"),
    ]
)
root = APIRouter(prefix="/birds")
@root.get("/")
async def tempmain()->HTMLResponse:
    return root_html.html()
    
@root.get("/owl")
async def tempmain()->HTMLResponse:
    return HTMLResponse("ooo")

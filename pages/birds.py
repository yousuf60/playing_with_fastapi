from fastapi import APIRouter
from .shared import *

root_html = link_list(
    [
        ("./owl","owl"),
    ]
)
root = APIRouter(prefix="/birds")
@root.get("/")
async def tempmain()->str:
    return root_html
    
@root.get("/owl")
async def tempmain()->str:
    return HTMLResponse("ooo")

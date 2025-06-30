from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from typing import Annotated
import pathlib
from .shared import *

title = "cats"

root_html = link_list(
    [
        ("pet","pets"),
        ("lion","lions"),
    ]
)

root = APIRouter(prefix="/"+title)

@root.get("/")
async def main() -> HTMLResponse:
    return HTMLResponse(root_html)
    
@root.get("/pet/")
async def pets(file:Annotated[str|None,Query()] = None ) :    
    #test edite later
    print(file)
    if file and pathlib.Path("./data/cats/pet_cat/" + file).exists():
        return  FileResponse("./data/cats/pet_cat/" + file)
    
    return HTMLResponse("mewmew" + list_files("cats/pet_cat") )




@root.get("/lion")
async def lion() -> HTMLResponse:
    return HTMLResponse("roar")






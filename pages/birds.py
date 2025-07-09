from .shared import *
from fastapi import APIRouter, Depends
title = "birds"
root_html = link_list(Roots.birds)
root = APIRouter(prefix="/"+title)


@root.get("/")
async def tempmain()->HTMLResponse:
    return root_html.html()
    
@root.get("/ducks/")
async def tempmain(file: Annotated[FL|None,
                    Depends(FL(title, Names.ducks[0]))])->HTMLResponse:
    if file.fl:
            return file.fl 
            
    return (HTMLHolder("<center><a href='https://duckduckgo.com'>duck duck daaack</a></center> ") +
     list_files(file.title, file.folder)).html()

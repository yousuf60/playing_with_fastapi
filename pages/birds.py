from typing import Annotated
from .shared import *
from fastapi import APIRouter

title = Names.birds
root_html = link_list(Roots.birds)
root = APIRouter(prefix="/"+title)


@root.get("/")
async def main_birds()->HTMLResponse:
    return root_html.html()
    


@root.get("/"+Names.owls[0]+"/")
async def owwl(file: Annotated[FL|None,
                    Depends(FL(title, Names.owls[0]))]):
    if file:
            return file
            
    return (HTMLHolder("ooowww") + list_files(title, Names.owls[0])).html()


@root.get("/"+Names.ducks[0]+"/")
async def duckduck(file: Annotated[FL|None,
                    Depends(FL(title, Names.ducks[0]))]):
    if file:
            return file
            
    return (HTMLHolder("<center><a href='https://duckduckgo.com'>duck duck gooooooo</a></center> ") +
     list_files(title, Names.ducks[0])).html()


from typing import Annotated
from .shared import *
from fastapi import APIRouter

title = Names.cats
root_html = link_list(
    Roots.cats
)

root = APIRouter(prefix="/"+title)


@root.get("/")
async def main_cats() -> HTMLResponse:
    return root_html.html()
    
@root.get("/"+Names.pets[0]+"/")
async def pets(file: Annotated[FL|None,
                    Depends(FL(title, Names.pets[0]))],
                    ) :
    if file:
        return file
        
    return (HTMLHolder("mewmew") + list_files(title, Names.pets[0])).html()

@root.get("/"+Names.lions[0]+"/")
async def lion(file: Annotated[FL|None,
                        Depends(FL(title, Names.lions[0]))],
                                ) :    
    if file:
        return file
        
    return (HTMLHolder("roar") + list_files(title, Names.lions[0])).html()



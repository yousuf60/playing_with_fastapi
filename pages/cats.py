from fastapi import APIRouter, Query, Depends
from typing import Annotated
from .shared import *

title = "cats"

root_html = link_list(
    [
        ("pet","pets"),
        ("lion","lions"),
    ]
)

root = APIRouter(prefix="/"+title)

#will be moved later to //shared
class FL:
    folder: str 
    title: str 
    fl = None
    def __init__(self, title, folder):
        self.folder = folder
        self.title = title
        

    async def file(self,file:Annotated[str|None,Query()]=None):
        
        if file:
            self.fl = get_file(self.title, self.folder, file)
        return self
    
    

@root.get("/")
async def main() -> HTMLResponse:
    return root_html.html()
    
@root.get("/pet/")
async def pets(file:Annotated[FL|None,
                    Depends(FL(title, "pet_cat").file)] = None ) :    

    if file.fl:
        return file.fl
        

    return (HtmlHolder("mewmew") + list_files(file.title, file.folder)).html()



@root.get("/lion/")
async def lion(file:Annotated[FL|None,
                                Depends(FL(title, "lions").file)] = None ) :    
    if file.fl:
        return file.fl 
    return (HtmlHolder("roar") + list_files(file.title, file.folder)).html()






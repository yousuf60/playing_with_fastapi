import os
import pathlib
from typing import Annotated
from struct import Struct
import fastapi
from fastapi import Query
from fastapi.responses import HTMLResponse

# name , textorcomment in case of editions
class Names(Struct):
    birds = "birds"
    cats = "cats"
    ducks = ("ducks", "duck duck")
    lions = ("lions", "lions")
    pets = ("pets", "pets")
    

# path of the roots
class Roots(Struct):
    birds = (Names.ducks, )
    cats = (Names.lions, Names.pets)



#takes list to turn it into html links returning htmlholder class
def link_list(lst: list):
    text = ""
    
    #[(path,text),....]
    for p,t in lst:
        text += f"""<br> <a href="./{p}">{t}</a>"""
    
    return HTMLHolder(text)
    

# join path together
def dt_path(*path):
    return os.path.join("./data",*path)


def list_files(*path):
    lst = os.listdir(dt_path(*path))

    print(lst)
    #make sure to name the first folder as the root title 
    return link_list(zip(["?file="+i.split("/")[0] for i in lst],lst))

    
# make a file respnse of file name and folder
def get_file(*path):
    fl = dt_path(*path)
    if pathlib.Path(fl).exists():
        return  fastapi.responses.FileResponse(fl)
    return 0

# hold string to call or get htmlresponse of it
class HTMLHolder:
    text: str
    def __init__(self, text: str):
        self.text = text
        
    def html(self):
        return HTMLResponse(self.text)

    def __call__(self):
        return self.text
        
    def __add__(self, txt):
        self.text += txt.text
        return self
        




#mini file getter for dependincies 
class FL:
    folder: str 
    title: str 
    fl = None
    def __init__(self, title, folder):
        self.folder = folder
        self.title = title
        
    async def __call__(self,file: Annotated[str|None,Query()]=None):
        if file:
            self.fl = get_file(self.title, self.folder, file)
        return self
    
    


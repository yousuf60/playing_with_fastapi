from fastapi.responses import HTMLResponse
import os
#takes list to turn it into html links 
def link_list(lst: list):
    text = ""
    
    #[(path,text),....]
    for p,t in lst:
        text += f"""<br> <a href="./{p}">{t}</a>"""
    
    return text
    


def listdir(path:str):
    return os.listdir("./data/"+path)
    
def list_files(path: str):
    lst = listdir(path)
    
    #make sure to name the first folder as the root title 
    return link_list(zip(["?file="+i.split("/")[0] for i in lst],lst))
    



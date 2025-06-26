from fastapi.responses import HTMLResponse

#takes list to rutn it into html links 
def link_list(lst: list):
    text = ""
    
    #[(path,text),....]
    for p,t in lst:
        text += f"""<a href="{p}">{t}</a>\n"""
    
    return HTMLResponse(text)
    



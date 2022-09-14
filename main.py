from typing import Union

from fastapi import FastAPI,Request
from todo import todo_router
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Creating new instance of FASTAPI

app = FastAPI()

templates = Jinja2Templates(directory="templates") 
# app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/admin")
async def admin_view(request: Request):
     return templates.TemplateResponse("base.html",{"request":request})

# @app.post("/admin/login/")
# async def admin_post(username:str,password:str):
#      username='nafisa'
#      password='pass'
#      # role='Superadmin'
#      return {{'username':username,'password':password}}

@app.post("/admin/login/{username}/{password}/{role}")
async def admin_read(request: Request, username: str,password:str,role:str):
#     username="admin" 
    return templates.TemplateResponse("base.html", {"request": request,"username":username,"password":username,"role":role})

@app.get("/admin/login/{username}/{password}/{role}")
async def admin_read(request: Request, username: str,password:str,role:str):
#     username="admin" 
    return templates.TemplateResponse("base.html", {"request": request,"username":username,"password":username,"role":role})
# app.include_router(todo_router)
# @app.get("/")
# async def say_hello() -> dict:
#     return {"message": "Hello!"}
# app.include_router(todo_router)



# # app = FastAPI()

# # @app.get("/")
# # async def welcome() -> dict:
# #     return { "message": "Hello World"}
# # @app.get('/')
# # def index():
# #     # return 'heyy'
# #     return {'database':{'date':{'name':'Nafisa','id':'171'}}}

# @app.get('/about')
# def about():

#     return {'data':{'about page'}}
#     return {'data':'about page'}



# # @app.get("/")
# # def read_root():
# #     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

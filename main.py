 
from typing import Union

from fastapi import FastAPI,Request,HTTPException,Path, Depends
from fastapi.templating import Jinja2Templates
from model import Todo,TodoItem,TodoItems
from todo import todo_router
 

# Creating new instance of FASTAPI

todo_router = FastAPI()

todo_list=[]

templates = Jinja2Templates(directory="templates/") 
# app.mount("/static", StaticFiles(directory="static"), name="static")
@todo_router.post("/todo")
async def add_todo(request:Request,todo:Todo=Depends(Todo.as_form) ):
    todo.id=len(todo_list) +1
    todo_list.append(todo)
    return templates.TemplateResponse("base.html",
    {
        "request":request,
        "todos":todo_list
    })
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse("base.html", {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("base.html", {
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(request: Request, todo_data: TodoItem,
                      todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(request: Request, todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }



# @app.get("/admin")
# async def admin_view(request: Request):
#      return templates.TemplateResponse("base.html",{"request":request})

# @app.post("/admin/login/")
# async def admin_post(username:str,password:str):
#      username='nafisa'
#      password='pass'
#      # role='Superadmin'
#      return {{'username':username,'password':password}}

# @app.post("/admin/login ")
# async def admin_read(request: Request, username: str,password:str,role:str):
# #     username="admin" 
#     return templates.TemplateResponse("base.html", {"request": request,"username":username,"password":username })

# @app.get("/admin/login")
# async def admin_read(request: Request, username: str,password:str,role:str):
# #     username="admin" 
#     return templates.TemplateResponse("base.html", {"request": request,"username":username,"password":username})
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

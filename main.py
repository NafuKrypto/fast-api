from typing import Union

from fastapi import FastAPI
from todo import todo_router
# Creating new instance of FASTAPI
 
app = FastAPI()
 

@app.get("/")
async def say_hello() -> dict:
    return {"message": "Hello!"}
app.include_router(todo_router)



# app = FastAPI()

# @app.get("/")
# async def welcome() -> dict:
#     return { "message": "Hello World"}
# @app.get('/')
# def index():
#     # return 'heyy'
#     return {'database':{'date':{'name':'Nafisa','id':'171'}}}

# @app.get('/about')
# def about():

    # return {'data':{'about page'}}
    # return {'data':'about page'}



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

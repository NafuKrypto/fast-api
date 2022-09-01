from typing import Union

from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    # return 'heyy'
    return {'database':{'date':{'name':'Nafisa','id':'171'}}}

@app.get('/about')
def about():

    # return {'data':{'about page'}}
    return {'data':'about page'}



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

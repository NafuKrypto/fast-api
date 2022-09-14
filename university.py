from typing import Union

from fastapi import FastAPI, APIRouter
# Creating new instance of FASTAPI
 
 
uni_router=APIRouter()
uni_list = []
@todo_router.post("/uni")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}
@todo_router.get("/uni")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
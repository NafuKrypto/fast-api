from email import message
from fastapi import FastAPI
from customers import customer_router
app=FastAPI()

 


app.include_router(customer_router)
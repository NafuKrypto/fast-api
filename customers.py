from fastapi import APIRouter

 
customer_router=APIRouter()
customer_list=[]
@customer_router.post("/customer")
async def customer_add(customer:dict)->dict:
    customer_list.append(customer) 
    return {"customers":"done"}

@customer_router.get("/customer")
async def customer_view()->dict:
     
    return {"customers":customer_list}
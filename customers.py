from fastapi import FastAPI, Form
from fastapi import APIRouter, Path
from customer_model import Customer

customer_router = APIRouter()
customer_list = []


# @customer_router.post("/customer")
# async def customer_add(customer: dict) -> dict:
#     customer_list.append(customer)
#     return {"customers": "done"}
@customer_router.post("/customer")
async def customer_add(customer: Customer) -> dict:

    customer_list.append(customer)
    return {"customers": "customer post router"}


@customer_router.post("/customer/{customer_id}")
async def customer_add_id(customer: Customer, customer_id: int) -> dict:

    # customer_list.append(customer)
    customer.customer.info.id = customer_id
    return {"customers":  customer_id, "customer": customer}


@customer_router.get("/customer/{customer_id}")
async def customer_view_id(customer_id: int) -> dict:
    # input()
    return {"customers": customer_id}


@customer_router.get("/customer")
async def customer_view() -> dict:

    return {"customers": customer_list}

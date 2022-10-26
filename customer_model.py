from pydantic import BaseModel


class Test(BaseModel):
    id: str
    Name: str
    Age: str
    Gender: str
    Phonenumber: str


class CustomerInfo(BaseModel):
    info: Test


class Customer(BaseModel):
    """Nested Model"""
    customer: CustomerInfo
    CustomerType: str
    Status: str

    # class Config:
    #     Schema_extra = {
    #         "customer": {
    #             "info": {
    #                 "id": "hfdf",
    #                 "Name": "dfdf",
    #                 "Age": "dsfsdf",
    #                 "Gender": "strsdfing",
    #                 "Phonenumber": "dsfsdf"
    #             }
    #         },
    #         "CustomerType": "sdfsdf",
    #         "Status": "sdfsd"
    #     }

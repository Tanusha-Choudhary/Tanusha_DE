from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Customer API",
    description="Simple API for customer API",
    version="1.0"
)
# -----------------------------
# Pydantic Models
# -----------------------------
class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    age: int
class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

# -----------------------------
# Sample Data
# -----------------------------
customers = [
    {
        "id": 1,
        "name": "John",
        "email": "john@gmail.com",
        "age": 30
    },
    {
        "id": 2,
        "name": "Alice",
        "email": "alice@gmail.com",
        "age": 28
    },
    {
        "id": 3,
        "name": "David",
        "email": "david@gmail.com",
        "age": 35
    }
]

# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
async def root():
    return {"message": "Customer API is running"}

# -----------------------------
# GET - Get all customers
# -----------------------------
@app.get("/customers")
async def get_customers():
    return {"customers": customers}
# -----------------------------
# GET - Get customer by ID
# -----------------------------

@app.get("/customers/{id}")
async def get_customer(id: int):
    for customer in customers:
        if customer["id"] == id:
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")
# -----------------------------
# POST - Create customer
# -----------------------------
@app.post("/customers")
async def create_customer(customer: CustomerCreate):
    new_id = max([i["id"] for i in customers],default=0) +1
    new_customer = {
        "id": new_id,
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
        "age": customer.age
    }
    customers.append(new_customer)
    return new_customer
# -----------------------------
# PUT - Update customer
# -----------------------------

@app.put("/customers/{customer_id}")
async def update_customer(
    customer_id: int,
    customer: CustomerUpdate
):

    for existing_customer in customers:

        if existing_customer["id"] == customer_id:

            if customer.name is not None:
                existing_customer["name"] = customer.name

            if customer.email is not None:
                existing_customer["email"] = customer.email

            if customer.age is not None:
                existing_customer["age"] = customer.age

            return existing_customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )


# -----------------------------
# DELETE - Delete customer
# -----------------------------

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):

    for customer in customers:

        if customer["id"] == customer_id:

            customers.remove(customer)

            return {
                "message": "Customer deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )
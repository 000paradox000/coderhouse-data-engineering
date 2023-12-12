from pydantic import BaseModel


class Customer(BaseModel):
    customerid: int
    name: str
    occupation: str | None = None
    email: str | None = None
    company: str | None = None
    phonenumber: str | None = None
    age: int | None = None

    class Config:
        from_attributes = True

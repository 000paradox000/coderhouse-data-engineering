from pydantic import BaseModel


class Call(BaseModel):
    callid:int
    agentid: int
    customerid: int
    pickedup: int | None = None
    duration: int | None = None
    productsold: int | None = None

    class Config:
        from_attributes = True

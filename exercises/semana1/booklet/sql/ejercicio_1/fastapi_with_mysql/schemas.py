from pydantic import BaseModel


class Agent(BaseModel):
    agentid: int
    name: str

    class Config:
        from_attributes = True
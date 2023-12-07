from sqlalchemy import Column, Integer, String
from .database import Base


class Agent(Base):
    __tablename__ = 'agents'
    agentid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

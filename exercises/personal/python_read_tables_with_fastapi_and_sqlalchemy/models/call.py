from sqlalchemy import Column, Integer, String

from .database import Base


class Call(Base):
    __tablename__ = 'calls'
    callid = Column(Integer, primary_key=True)
    agentid = Column(Integer)
    customerid = Column(Integer)
    pickedup = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True)
    productsold = Column(Integer, nullable=True)

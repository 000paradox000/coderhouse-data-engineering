from sqlalchemy import Column, Integer, String

from .database import Base


class Customer(Base):
    __tablename__ = 'customers'
    customerid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    occupation = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    company = Column(String(50), nullable=True)
    phonenumber = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)

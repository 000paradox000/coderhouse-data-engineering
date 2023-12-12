from .base import db


class Customer(db.Model):
    __tablename__ = 'customers'
    customerid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    occupation = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    company = db.Column(db.String(50), nullable=True)
    phonenumber = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=True)

from .base import db


class Call(db.Model):
    __tablename__ = 'calls'
    callid = db.Column(db.Integer, primary_key=True)
    agentid = db.Column(db.Integer)
    customerid = db.Column(db.Integer)
    pickedup = db.Column(db.Integer, nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    productsold = db.Column(db.Integer, nullable=True)

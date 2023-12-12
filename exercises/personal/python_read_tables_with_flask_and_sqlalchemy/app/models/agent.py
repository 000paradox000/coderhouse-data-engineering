from .base import db


class Agent(db.Model):
    __tablename__ = 'agents'
    agentid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

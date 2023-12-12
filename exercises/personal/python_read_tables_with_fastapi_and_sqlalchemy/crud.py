from sqlalchemy.orm import Session

import models


def get_agents(db: Session):
    return db.query(models.Agent).all()


def get_customers(db: Session):
    return db.query(models.Customer).all()


def get_calls(db: Session):
    return db.query(models.Call).all()

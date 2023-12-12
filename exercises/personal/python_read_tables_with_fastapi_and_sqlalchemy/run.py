import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--engine", choices=["postgres", "mysql", "mssql"])
args = parser.parse_args()
engine_option = args.engine

if engine_option == "postgres":
    os.environ["SQLALCHEMY_DATABASE_URL"] = r"postgresql://coderhouse:coderhouse@db_postgres:5432/coderhouse"
elif engine_option == "mysql":
    os.environ["SQLALCHEMY_DATABASE_URL"] = r"mysql+mysqlconnector://coderhouse:coderhouse@db_mysql:3306/coderhouse"
elif engine_option == "mssql":
    os.environ["SQLALCHEMY_DATABASE_URL"] = r"mssql+pymssql://coderhouse:C0d3rhous3@db_mssql:1433/coderhouse"

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import schemas
from models.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/agents/", response_model=list[schemas.Agent])
def list_agents(db: Session = Depends(get_db)):
    return crud.get_agents(db)


@app.get("/customers/", response_model=list[schemas.Customer])
def list_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)


@app.get("/calls/", response_model=list[schemas.Call])
def list_calls(db: Session = Depends(get_db)):
    return crud.get_calls(db)


def main():
    import uvicorn

    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()

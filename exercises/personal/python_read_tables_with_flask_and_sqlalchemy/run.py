import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=["postgres", "mysql", "mssql"])
    args = parser.parse_args()

    engine_option = args.engine

    if engine_option == "postgres":
        os.environ["SQLALCHEMY_DATABASE_URI"] = r"postgresql://coderhouse:coderhouse@db_postgres:5432/coderhouse"
    elif engine_option == "mysql":
        os.environ["SQLALCHEMY_DATABASE_URI"] = r"mysql+mysqlconnector://coderhouse:coderhouse@db_mysql:3306/coderhouse"
    elif engine_option == "mssql":
        os.environ["SQLALCHEMY_DATABASE_URI"] = r"mssql+pymssql://coderhouse:C0d3rhous3@db_mssql:1433/coderhouse"

    from app.main import create_app

    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()

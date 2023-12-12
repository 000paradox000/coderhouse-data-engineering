import psycopg2

def main():
    print("=" * 50)
    print("Postgres Database")
    print("=" * 50)
    db_params = {
        'host': 'db_postgres',
        'port': '5432',
        'database': 'coderhouse',
        'user': 'coderhouse',
        'password': 'coderhouse'
    }

    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    with open("/opt/sql/ejercicio.sql", "r") as fh:
        query = fh.read()

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print("-" * 50)
    print("")
    print("")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

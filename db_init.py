import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(dbname, username, password):
    # Create a connection to the PostgreSQL
    try:
        print("Establishing a connection to the PostgreSQL Server")
        connection = psycopg2.connect(
            host='localhost', user=username, password=password)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        print(f"Creating the '{dbname}' database")
        # Create the database with the passed database name
        create_database_statement = F"CREATE DATABASE {dbname}"
        cursor.execute(create_database_statement)

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Unable to create the database,", error)

    finally:
        # Closing the database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def create_table(dbname, table_name, username, password):
    # Create a connection to the PostgreSQL
    try:
        print(f"Establishing a connection to the '{dbname}' database")
        connection = psycopg2.connect(
            host='localhost', user=username, password=password, database=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        print(f"Creating the '{table_name}' table")
        # Create a table in passed database with the passed table name
        create_table_statement = F"""CREATE TABLE IF NOT EXISTS {table_name}(
            id serial PRIMARY KEY,
            from_currency varchar(5) NOT NULL,
            to_currency varchar(5) NOT NULL,
            request_date date NOT NULL,
            exchange_rate real NOT NULL
        )
        """
        cursor.execute(create_table_statement)

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Unable to create the table,", error)

    finally:
        # Closing the database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


username = input("Enter the PostgreSQL server username:")
password = input("Enter the PostgreSQL server password:")
dbname = "currencies"
table_name = "rates"
create_database(dbname, username, password)
create_table(dbname, table_name, username, password)

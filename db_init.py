import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(dbname):
    # Create a connection to the PostgreSQL
    try:
        connection = psycopg2.connect(
            host='localhost', user="postgres", password="root")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        # Create the database with the passed database naem
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


def create_table(dbname, table_name):
    # Create a connection to the PostgreSQL
    try:
        connection = psycopg2.connect(
            host='localhost', user="postgres", password="root", database=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        # Create a table in passed database with the passed table name
        create_table_statement = F"""CREATE TABLE IF NOT EXISTS {table_name}(
            id serial PRIMARY KEY,
            from_currency varchar(5) NOT NULL,
            to_currency varchar(5) NOT NULL,
            request_date date NOT NULL
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


dbname = "currencies"
table_name = "rates"
create_database(dbname)
create_table(dbname, table_name)

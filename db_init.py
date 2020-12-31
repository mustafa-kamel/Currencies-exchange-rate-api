# This script will create the requried database and database tables
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# This function will create the database


def create_db(dbname):
    connection = cursor = ''
    try:
        # Connect to the database server
        connection = psycopg2.connect(
            host='localhost', user='postgres', password='root')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Obtain a DB Cursor
        cursor = connection.cursor()

        # Create the database statement
        sqlCreateDatabase = F"create database {dbname};"

        # Create a database
        cursor.execute(sqlCreateDatabase)

    except:
        print("Unable to connect to the PostgreSQL server")
    finally:
        if connection:
            cursor.close()
            connection.close()


def create_table(dbname, table_name):
    connection = cursor = ''
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host='localhost', user='postgres', password='root', database=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Obtain a DB Cursor
        cursor = connection.cursor()

        # Create the table statement
        sqlCreateTable = F"""create table if not exists {table_name} (
            id serial PRIMARY KEY,
            from_currency varchar(5) not null,
            to_currency varchar(5) not null,
            exchange_rate real,
            request_date date not null
        )"""

        # Create a table in the PostgreSQL database
        cursor.execute(sqlCreateTable)

    except Exception as error:
        print("Unable to connect to the PostgreSQL server")
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()


dbname = "currencies"
table_name = "rates"
create_db(dbname)
create_table(dbname, table_name)

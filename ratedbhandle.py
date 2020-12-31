# This script will handle all the databse queries

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = ''
dbname = "currencies"


def connect_db():
    global connection
    global dbname
    # Create a connection to the PostgreSQL
    try:
        connection = psycopg2.connect(
            host='localhost', user="postgres", password="root", database=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # If the connection succeed return the cursor
        cursor = connection.cursor()
        return cursor
    except (Exception, psycopg2.Error) as error:
        print("Unable to establish a connection,", error)


def execute_query(statement, args):
    cursor = connect_db()
    cursor.execute(statement, args)
    return cursor


def close_connection(cursor):
    global connection
    # Closing the database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def execute_select(statement, condition):
    cursor = execute_query(statement, condition)
    result = cursor.fetchone()
    close_connection(cursor)
    return result

def execute_insert(statement, data):
    cursor = execute_query(statement, data)
    row_count = cursor.rowcount
    close_connection(cursor)
    return row_count

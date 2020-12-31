import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = ''


def connect_db(dbname="currencies"):
    global connection
    try:
        # Connect to the database server
        connection = psycopg2.connect(
            host='localhost', user='postgres', password='root', database=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        connection = connection
        # Obtain a DB Cursor
        cursor = connection.cursor()
        return cursor
    except:
        print("Unable to connect to the PostgreSQL server")


def close_connection(cursor):
    global connection
    if connection:
        cursor.close()
        connection.close()


def execute_select(statement, condition):
    cursor = connect_db()
    cursor.execute(statement, condition)
    result = cursor.fetchone()
    close_connection(cursor)
    return result


def execute_insert(statement, data):
    cursor = connect_db()
    cursor.execute(statement, data)
    row_count = cursor.rowcount
    close_connection(cursor)
    return row_count

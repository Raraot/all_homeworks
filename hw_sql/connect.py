from psycopg2 import connect,  Error
from contextlib import contextmanager

@contextmanager
def create_connect():
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', database='postgres', password='5225')
        yield conn
    except Error as err:
        print(err)
    finally:
        conn.close


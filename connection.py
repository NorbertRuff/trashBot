import os

import psycopg2
import psycopg2.extras


def open_database():
    try:
        database_url = os.environ['DATABASE_URL']
        ssl_mode = os.environ['DATABASE_SSL']
        connection = psycopg2.connect(database_url, sslmode=ssl_mode)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper


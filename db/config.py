from psycopg2 import connect


class DBconfig:
    DB_NAME = 'movie_bot'
    DB_USER = 'postgres'
    DB_HOST = 'localhost'
    DB_PORT = 5432                  
    DB_PASSWORD = 1
    connect = connect(
        db_name=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cur = connect.cursor()

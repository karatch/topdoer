import sqlite3

DB_NAME = 'incidents'
DB_FILE_NAME = 'incidents.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE_NAME)
    # получаем данные в виде словаря
    conn.row_factory = sqlite3.Row
    return conn

get_db_connection()
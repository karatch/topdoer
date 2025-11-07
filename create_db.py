import sqlite3
from connect_db import DB_NAME, DB_FILE_NAME

conn = sqlite3.connect(DB_FILE_NAME)
cursor = conn.cursor()

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {DB_NAME} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    stat TEXT NOT NULL,
    source TEXT NOT NULL,
    datetime TEXT NOT NULL
)
""")

conn.commit()
conn.close()
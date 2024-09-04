import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "memory_info.db"


@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()


def create_tables():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp INTEGER NOT NULL,
                total INTEGER NOT NULL,
                free INTEGER NOT NULL,
                used INTEGER NOT NULL
            )
        """)
        conn.commit()
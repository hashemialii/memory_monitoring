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
                timestamp TEXT NOT NULL,
                total INTEGER NOT NULL,
                free INTEGER NOT NULL,
                used INTEGER NOT NULL
            )
        """)
        conn.commit()


def reset_autoincrement():
    """Reset the AUTOINCREMENT counter for the memory_info table."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='memory_info'")
        conn.commit()

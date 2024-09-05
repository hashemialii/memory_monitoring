from datetime import datetime
from app.database import get_db


def insert_memory_info(total, free, used):
    with get_db() as conn:
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO memory_info (timestamp, total, free, used)
            VALUES (?, ?, ?, ?)
        """, (timestamp, total, free, used))
        conn.commit()


def get_last_n_records(n):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, timestamp, total, free, used
            FROM memory_info
            ORDER BY timestamp DESC
            LIMIT ?
        """, [n])
        rows = cursor.fetchall()
        return rows


def clear_memory_info():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM memory_info")
        conn.commit()

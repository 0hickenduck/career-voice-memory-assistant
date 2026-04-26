import sqlite3
from datetime import datetime

DB_NAME = "career_memory.db"


def init_db():
    """Create the records table if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            category TEXT NOT NULL,
            raw_text TEXT NOT NULL,
            summary TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def save_record(category: str, raw_text: str, summary: str):
    """Save one record to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO records (created_at, category, raw_text, summary)
        VALUES (?, ?, ?, ?)
        """,
        (datetime.now().isoformat(timespec="seconds"), category, raw_text, summary),
    )

    conn.commit()
    conn.close()


def get_records():
    """Get all records, newest first."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, created_at, category, raw_text, summary
        FROM records
        ORDER BY created_at DESC
        """
    )

    records = cursor.fetchall()
    conn.close()

    return records
#!/usr/bin/env python3
import sqlite3

DB_FILE = "aos_cx_fun.db"

def setup_db():
    """This function is intended to only be ran once during intial set up."""
    with sqlite3.connect(DB_FILE) as conn:
        # WAL is Write-Ahead logging, so we can read/write concurrently
        conn.execute("PRAGMA journal_mode=WAL")

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS interface_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                interface TEXT,
                tx_bytes INTEGER,
                rx_bytes INTEGER,
                Bps REAL,
                util_pct REAL,
                timestamp TEXT
            );
        """)

        conn.commit()

if __name__ == "__main__":
    setup_db()
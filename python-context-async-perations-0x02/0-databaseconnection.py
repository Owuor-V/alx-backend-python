#!/usr/bin/env python3
"""
Class-based context manager to handle opening and closing
SQLite database connections automatically.
"""

import sqlite3

class DatabaseConnection:
    """Custom context manager for SQLite database connections."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        """Open the database connection when entering the context."""
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the database connection when exiting the context."""
        if self.conn:
            self.conn.close()
        # Returning False makes sure exceptions (if any) propagate
        return False


# ✅ Usage example
if __name__ == "__main__":
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print("Users in DB:")
        for row in results:
            print(row)

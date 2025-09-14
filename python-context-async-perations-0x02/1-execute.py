#!/usr/bin/env python3
"""
Reusable context manager that executes a given SQL query
and returns the results automatically.
"""

import sqlite3


class ExecuteQuery:
    """Context manager for executing a query with parameters."""

    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        """Open DB connection, execute query, and fetch results."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results  # ✅ return results directly for usage inside with

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the cursor and connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        return False  # don’t suppress exceptions


# ✅ Usage Example
if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    param = (25,)

    with ExecuteQuery("users.db", query, param) as results:
        print("Users older than 25:")
        for row in results:
            print(row)

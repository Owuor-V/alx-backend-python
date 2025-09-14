#!/usr/bin/python3
import sqlite3
import functools


def with_db_connection(func):
    """
    Decorator to automatically open and close
    the SQLite database connection.
    It passes the connection object as the first argument
    to the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


# ---- Test run ----
if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print("User with ID 1:", user)

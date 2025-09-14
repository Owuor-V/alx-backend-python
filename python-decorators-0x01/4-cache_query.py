import time
import sqlite3
import functools

# Global cache dictionary
query_cache = {}

def with_db_connection(func):
    """Decorator to handle opening and closing DB connection."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def cache_query(func):
    """Decorator to cache query results."""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print(f"Cache hit for query: {query}")
            return query_cache[query]   # return cached result
        else:
            print(f"Cache miss for query: {query}")
            result = func(conn, query, *args, **kwargs)
            query_cache[query] = result   # store in cache
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call → executes query and caches result
users = fetch_users_with_cache(query="SELECT * FROM users")
print("First call result:", users)

# Second call → retrieves from cache instead of hitting DB
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print("Second call result (from cache):", users_again)

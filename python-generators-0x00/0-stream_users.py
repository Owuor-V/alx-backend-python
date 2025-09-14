#!/usr/bin/python3
import mysql.connector

def stream_users():
    """
    Generator function to fetch rows one by one from user_data table
    """
    # connect to the ALX_prodev database
    conn = mysql.connector.connect(
        host="localhost",       # adjust if needed
        user="root",            # your MySQL username
        password="Victor",    # your MySQL password
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)  # rows will come back as dictionaries

    cursor.execute("SELECT * FROM user_data")

    # yield each row one by one
    for row in cursor:
        yield row

    cursor.close()
    conn.close()

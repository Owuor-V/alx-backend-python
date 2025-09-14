#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator function that fetches rows in batches from user_data table
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Victor",   # <-- replace with your MySQL password
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data")
    while True:
        rows = cursor.fetchmany(batch_size)  # fetch rows in batch
        if not rows:
            break
        yield rows  # yield the whole batch

    cursor.close()
    conn.close()


def batch_processing(batch_size):
    """
    Process each batch: filter users over the age of 25
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)

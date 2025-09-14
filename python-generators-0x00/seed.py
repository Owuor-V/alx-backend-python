import mysql.connector
import csv
import uuid

def connect_db():
    """Connects to MySQL server (not specific DB)"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Victor"  # replace with your MySQL root password
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Victor",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            user_id = str(uuid.uuid4())
            name, email, age = row
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE name=name;
            """, (user_id, name, email, age))
    connection.commit()
    cursor.close()

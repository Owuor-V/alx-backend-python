# Python Generators – Seeding Database

This project sets up a MySQL database (`ALX_prodev`) with a `user_data` table and seeds it with data from a CSV file.

## Files
- **seed.py** → Contains functions to:
  - Connect to MySQL
  - Create the `ALX_prodev` database
  - Create the `user_data` table
  - Insert data from `user_data.csv`
- **0-main.py** → Runner script provided for testing.

## Functions
- `connect_db()` → Connects to MySQL server.
- `create_database(connection)` → Creates `ALX_prodev` database if not exists.
- `connect_to_prodev()` → Connects to the `ALX_prodev` database.
- `create_table(connection)` → Creates `user_data` table if not exists.
- `insert_data(connection, csv_file)` → Inserts rows from CSV into `user_data`.

## Example Run
```bash
$ ./0-main.py
connection successful
Table user_data created successfully
Database ALX_prodev is present
[('UUID1', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67), ...]

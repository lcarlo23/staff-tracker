import sqlite3


def initialize_db():
    # Connect to the database
    connection = sqlite3.connect("directory.db")
    cursor = connection.cursor()

    # Create table if not already existing
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    salary REAL
    )""")
    connection.commit()

    # Close connection to db
    connection.close()

import sqlite3


def create_connection():
    # Connect to the db
    connection = sqlite3.connect("directory.db")
    cursor = connection.cursor()

    return connection, cursor


def initialize_db():
    # Connect db
    connection, cursor = create_connection()

    # Create table if not already exists
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    salary REAL
    )""")

    # Commit and close db
    connection.commit()
    connection.close()


def add_employee(name, role, salary):
    # Connect db
    connection, cursor = create_connection()

    # Add employee to db
    cursor.execute(
        """INSERT INTO employees (
                   name,
                   role,
                   salary
                   ) VALUES (
                   ?,
                   ?,
                   ?
                   )""",
        (name, role, salary),
    )

    # Commit and close db
    connection.commit()
    connection.close()


def get_all_employees():
    # Connect db
    connection, cursor = create_connection()

    # Retrieve employees
    cursor.execute("""SELECT * FROM employees""")
    employees = cursor.fetchall()

    # Close db and return employees
    connection.close()
    return employees


def get_employee(employee_id):
    # Connect db
    connection, cursor = create_connection()

    # Retrieve employee
    cursor.execute("""SELECT * FROM employees WHERE id = ? """, (employee_id,))
    employee = cursor.fetchall()

    # Close db and return employees
    connection.close()
    return employee

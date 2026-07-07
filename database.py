import sqlite3

### MANAGE DATABASE ###


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


### ADD, EDIT, DELETE EMPLOYEES ###


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


def edit_employee(id, name, role, salary):
    # Connect db
    connection, cursor = create_connection()

    # Update employee
    cursor.execute(
        """UPDATE employees 
                   SET name = ?,
                   role = ?,
                   salary = ?
                   WHERE id = ? """,
        (name, role, salary, id),
    )

    # Commit and close db
    connection.commit()
    connection.close()


def delete_employee(id):
    # Connect db
    connection, cursor = create_connection()

    # Delete employee
    cursor.execute("""DELETE FROM employees WHERE id = ?""", (id,))

    # Commit and close db
    connection.commit()
    connection.close()


### RETRIEVE DATA ###


def get_all_employees():
    # Connect db
    connection, cursor = create_connection()

    # Retrieve employees
    cursor.execute("""SELECT * FROM employees""")
    employees = cursor.fetchall()

    # Close db and return employees
    connection.close()
    return employees


def get_employee(id):
    # Connect db
    connection, cursor = create_connection()

    # Retrieve employee
    cursor.execute("""SELECT * FROM employees WHERE id = ? """, (id,))
    employee = cursor.fetchall()

    # Close db and return employees
    connection.close()
    return employee

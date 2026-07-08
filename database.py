import sqlite3

### MANAGE DATABASE ###


def create_connection():
    # Connect to the db
    connection = sqlite3.connect("directory.db")
    cursor = connection.cursor()

    return connection, cursor


def initialize_db():
    connection = None

    try:
        # Connect db
        connection, cursor = create_connection()

        # Create table if not already exists
        cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        salary REAL
        )""")

        # Update db
        connection.commit()

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()


### ADD, EDIT, DELETE EMPLOYEES ###


def add_employee(name, role, salary):
    connection = None

    try:
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

        # Update db
        connection.commit()

        return True

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

        return False

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()


def edit_employee(id, name, role, salary):
    connection = None

    try:
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

        # Update db
        connection.commit()

        return True

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

        return False

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()


def delete_employee(id):
    connection = None

    try:
        # Connect db
        connection, cursor = create_connection()

        # Delete employee
        cursor.execute("""DELETE FROM employees WHERE id = ?""", (id,))

        # Update db
        connection.commit()

        return True

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

        return False

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()


### RETRIEVE DATA ###


def get_all_employees():
    connection = None

    try:
        # Connect db
        connection, cursor = create_connection()

        # Retrieve employees
        cursor.execute("""SELECT * FROM employees""")
        employees = cursor.fetchall()

        # Return employees
        return employees

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()


def get_employee(id):
    connection = None

    try:
        # Connect db
        connection, cursor = create_connection()

        # Retrieve employee
        cursor.execute("""SELECT * FROM employees WHERE id = ? """, (id,))
        employee = cursor.fetchall()

        # Return employee
        return employee

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()


def get_company_stats():
    connection = None

    try:
        # Connect db
        connection, cursor = create_connection()

        # Retrieve stats
        cursor.execute("""
                    SELECT
                        COUNT(*),
                        SUM(salary),
                        AVG(salary),
                        MAX(salary),
                        MIN(salary)
                    FROM employees
        """)

        # Return stats
        stats = cursor.fetchone()
        return stats

    except sqlite3.Error as error:
        # Display error if something goes wrong
        print(f"Database error: {error}")

    finally:
        # Close connection to db if connection was established
        if connection:
            connection.close()

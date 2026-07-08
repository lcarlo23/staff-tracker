import sqlite3

### MANAGE DATABASE ###


# Connect to database
def create_connection():
    # Connect to the db
    connection = sqlite3.connect("directory.db")
    cursor = connection.cursor()

    return connection, cursor


# Create table if not exists and catch errors if there is problems with database
def initialize_db():
    connection = None

    try:
        # Connect db
        connection, cursor = create_connection()

        # Create table if not already exists
        cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        salary REAL CHECK(salary >= 0)
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


# Add employee to database
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


# Update employee information
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


# Delete employee from database
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


# Retrieve all employees from database
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


# Retrieve employee from id
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


# Retrieve aggregate data from database
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

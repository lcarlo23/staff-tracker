import database as db
import locale

# Set locale for salary currency
locale.setlocale(locale.LC_ALL, "")


# Add employee to database
def add_employee():
    # Ask user to input data
    print()
    print("### Add New Employee ###")
    print()

    # Name Validation
    while True:
        name = input("Employee Full Name: ").strip()

        if not name:
            print()
            print("Error: Name cannot be empty!")
            print()
            continue

        if not name.replace(" ", "").isalpha():
            print()
            print("Error: Name must contain only letters!")
            print()
            continue

        break

    # Role Validation
    while True:
        role = input("Employee Role: ").strip()

        if not role:
            print()
            print("Error: Role cannot be empty!")
            print()
            continue

        if not role.replace(" ", "").isalpha():
            print()
            print("Error: Role must contain only letters!")
            print()
            continue

        break

    # Salary Validation
    while True:
        try:
            salary = float(input("Employee Salary (only numbers): "))
            if salary < 0:
                print()
                print("Error: Salary cannot be negative!")
                print()
                continue

            break

        except ValueError:
            print()
            print("Error: Please enter a valid decimal number for salary!")
            print()

    # Add user to db
    added = db.add_employee(name, role, salary)

    # Success/Fail message
    print()
    if added:
        print("Employee added successfully:")
        print(f"""
Name: {name}
Role: {role}
Salary: {locale.currency(salary, grouping=True)}""")
    else:
        print("There was an error adding the employee")
    print()


# Update employee information
def edit_employee():

    # Check db data
    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    # Ask user for ID and validate
    while True:
        try:
            id = int(input("Employee ID: "))
            if id < 0:
                print()
                print("Error: ID cannot be negative!")
                print()
                continue

            break

        except ValueError:
            print()
            print("Error: Please enter a valid integer number for the ID!")
            print()

    # Retrieve employee data
    employee_data = db.get_employee(id)

    # Check if employee with that id exists
    if not employee_data:
        print()
        print(f"Error: No employee found with ID {id}")
        print()
        return

    employee = employee_data[0]
    emp_name = employee[1]
    emp_role = employee[2]
    emp_salary = employee[3]

    # Ask user for edits
    print()
    print("Leave empty to keep the current values")
    print()

    # Name Validation
    while True:
        name = input(f"Full Name (current: {emp_name}): ").strip()

        if name == "":
            name = emp_name
            break
        if name.replace(" ", "").isalpha():
            break

        print("Error: Name must contain only letters!")

    # Role Validation
    while True:
        role = input(f"Role (current: {emp_role}): ").strip()

        if role == "":
            role = emp_role
            break
        if role.replace(" ", "").isalpha():
            break

        print("Error: Role must contain only letters!")

    # Salary Validation
    while True:
        salary = input(f"Salary (current: {emp_salary}): ").strip()

        if salary == "":
            salary = emp_salary
            break

        try:
            salary = float(salary)

            if salary < 0:
                print("Error: Salary cannot be negative!")
                continue
            break

        except ValueError:
            print("Error: Please enter a valid decimal number for salary!")

    # Update employee on db
    edited = db.edit_employee(id, name, role, salary)

    # Success/Fail message
    print()
    if edited:
        print(f"{name} updated successfully!")
    else:
        print("There was an error editing the employee")
    print()


# Delete employee from database
def delete_employee():

    # Check db data
    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    # Ask user for ID and validate
    while True:
        try:
            id = int(input("Employee ID: "))
            if id < 0:
                print()
                print("Error: ID cannot be negative!")
                print()
                continue

            break

        except ValueError:
            print()
            print("Error: Please enter a valid integer number for the ID!")
            print()

    # Retrieve employee data
    employee_data = db.get_employee(id)

    # Check if employee with that id exists
    if not employee_data:
        print()
        print(f"Error: No employee found with ID {id}")
        print()
        return

    # Ask for confirmation before deletion
    employee = employee_data[0]

    confirm = input(f"""
Are you sure you want to delete the following employee?
                
Name: {employee[1]}
Role: {employee[2]}
Salary: {locale.currency(employee[3], grouping=True)}

(Y/N): """)

    if confirm.upper() == "Y":
        deleted = db.delete_employee(id)

        # Success/Fail message
        print()
        if deleted:
            print(f"Employee deleted successfully!")
        else:
            print("There was an error deleting the employee")
        print()
    else:
        print()
        print("Deletion cancelled")
        print()
        return


# Retrieve employee data from db
def get_employee():

    # Check db data
    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    # Ask user for ID and validate
    while True:
        try:
            id = int(input("Employee ID: "))
            if id < 0:
                print()
                print("Error: ID cannot be negative!")
                print()
                continue

            break

        except ValueError:
            print()
            print("Error: Please enter a valid integer number for the ID!")
            print()

    # Retrieve employee data
    employee_data = db.get_employee(id)

    # Check if employee with that id exists
    if not employee_data:
        print()
        print(f"Error: No employee found with ID {id}")
        print()
        return

    # Retrieve employee from db
    employee = employee_data[0]

    # Print employee data
    print(f"""
        Name: {employee[1]}
        Role: {employee[2]}
        Salary: {locale.currency(employee[3], grouping=True)}
          """)


# Retrieve all employees data from db
def get_all_employees():

    # Check db data
    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    # Retrieve all table rows
    employees = db.get_all_employees()

    # Print all rows
    for employee in employees:
        print(f"""
              ID: {employee[0]}
              Name: {employee[1]}
              Role: {employee[2]}
              Salary: {locale.currency(employee[3], grouping=True)}
          """)


# Retrieve statistics from database
def get_company_stats():
    # Check db data
    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    stats = db.get_company_stats()

    print(f"""
### COMPANY STATISTICS ###
          
Employees: {stats[0]}
Total of Salaries: {locale.currency(stats[1], grouping=True)}
Average Salary: {locale.currency(stats[2], grouping=True)}
Highest Salary: {locale.currency(stats[3], grouping=True)}
Lowest Salary: {locale.currency(stats[4], grouping=True)}
          """)


# Check if there is data in the database
def is_db_empty():
    employees = db.get_all_employees()

    if len(employees) < 1:
        return True
    else:
        return False

import database as db
import locale

# Set locale for salary currency
locale.setlocale(locale.LC_ALL, "")


def add_employee():
    try:
        # Ask user to input data
        name = input("Employee Full Name: ")
        role = input("Employee Role: ")
        salary = float(input("Employee Salary (only numbers): "))

        # Add user to db
        added = db.add_employee(name, role, salary)

        # Success/Fail message
        print()
        if added:
            print(f"{name} added successfully!")
        else:
            print("There was an error adding the employee")
        print()
    except Exception as error:
        print(f"""
Error adding the employee:
{error}
""")


def get_employee():
    # Ask user for ID
    id = int(input("Employee ID: "))

    # Retrieve employee from db
    employee = db.get_employee(id)[0]

    # Print employee data
    print(f"""
        Name: {employee[1]}
        Role: {employee[2]}
        Salary: {locale.currency(employee[3], grouping=True)}
          """)


def edit_employee():
    # Ask user for ID
    id = int(input("Employee ID: "))

    # Retrieve employee data
    employee = db.get_employee(id)[0]
    emp_name = employee[1]
    emp_role = employee[2]
    emp_salary = employee[3]

    # Ask user for edits
    print()
    print("Leave empty to keep the current values")
    print()
    name = input(f"Full Name (current: {emp_name}): ").strip()
    role = input(f"Role (current: {emp_role}): ").strip()
    salary = input(f"Salary (current: {emp_salary}): ").strip()

    # Check if inputs are empty
    if name == "":
        name = emp_name

    if role == "":
        role = emp_role

    if salary == "":
        salary = emp_salary

    # Update employee on db
    edited = db.edit_employee(id, name, role, salary)

    # Success/Fail message
    print()
    if edited:
        print(f"{name} updated successfully!")
    else:
        print("There was an error editing the employee")
    print()


def delete_employee():

    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    # Ask user for ID
    id = int(input("Employee ID: "))

    employee = db.get_employee(id)[0]

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


def get_all_employees():

    if is_db_empty():
        print()
        print("There are no employees yet!")
        print()
        return

    employees = db.get_all_employees()

    for employee in employees:
        print(f"""
              ID: {employee[0]}
              Name: {employee[1]}
              Role: {employee[2]}
              Salary: {locale.currency(employee[3], grouping=True)}
          """)


def is_db_empty():
    employees = db.get_all_employees()

    if len(employees) < 1:
        return True
    else:
        return False

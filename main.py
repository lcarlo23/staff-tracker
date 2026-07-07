import database as db

# Check if database exists or create a new one
db.initialize_db()


# CLI menu

while True:
    print("### Welcome to Staff Tracker ###")
    print()
    print("1. Add new employee")
    print("2. Edit employee")
    print("3. Delete employee")
    print("4. Get all employees")
    print("5. Get an employee")
    print("6. Exit")
    print()

    selection = int(input("Select an option (1-6): "))

    if selection == 6:
        break

import database as db
import controller as ctrl

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

    match selection:
        case 1:
            ctrl.add_employee()
            input("Press Enter to return to main menu")
        case 2:
            ctrl.edit_employee()
            input("Press Enter to return to main menu")
        case 3:
            ctrl.delete_employee()
            input("Press Enter to return to main menu")
        case 4:
            ctrl.get_all_employees()
            input("Press Enter to return to main menu")
        case 5:
            ctrl.get_employee()
            input("Press Enter to return to main menu")
        case 6:
            break
        case _:
            print("Invalid option. Please select a number between 1 and 6.")
            print()

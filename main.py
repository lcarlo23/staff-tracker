import database as db
import controller as ctrl

# Check if database exists or create a new one
db.initialize_db()


# CLI menu
print()
print("### Welcome to Staff Tracker ###")

while True:
    print("""
### MAIN MENU ###
          
1. Add new employee
2. Edit employee
3. Delete employee
4. Get all employees
5. Get an employee
6. Exit
    """)

    selection = int(input("Select an option (1-6): "))

    match selection:
        case 1:
            ctrl.add_employee()
        case 2:
            ctrl.edit_employee()
        case 3:
            ctrl.delete_employee()
        case 4:
            ctrl.get_all_employees()
        case 5:
            ctrl.get_employee()
        case 6:
            break
        case _:
            print()
            print("Invalid option. Please select a number between 1 and 6.")
            print()

    input("Press Enter to return to main menu")

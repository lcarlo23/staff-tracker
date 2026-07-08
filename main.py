import database as db
import controller as ctrl

# Check if database exists or create a new one
db.initialize_db()


# CLI menu
print()
print("### Welcome to Staff Tracker ###")

# Menu logic
while True:
    print("""
### MAIN MENU ###
          
1. Add new employee
2. Edit employee
3. Delete employee          
4. Get employee data
5. Get all employees data
6. Company Statistics
    """)

    selection = int(input("Select an option (1-6, 0 to exit): "))

    match selection:
        case 0:
            break
        case 1:
            ctrl.add_employee()
        case 2:
            ctrl.edit_employee()
        case 3:
            ctrl.delete_employee()
        case 4:
            ctrl.get_employee()
        case 5:
            ctrl.get_all_employees()
        case 6:
            ctrl.get_company_stats()
        case _:
            print()
            print("Invalid option. Please select a number between 1 and 6.")
            print()

    input("Press Enter to return to main menu")

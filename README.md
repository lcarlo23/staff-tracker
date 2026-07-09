# Overview

Staff Tracker is a command-line program to manage a company's employee records. It connects to a local SQLite database to save all data. The program allows you to manage employee profiles and includes a statistics menu to see company totals and averages.

I created this project to improve my software engineering skills, specifically learning how to connect a Python application to a SQL database and organizing code using the MVC pattern.

### How to Use the Program

1. Run `main.py` to start the menu.
2. Type a number from 0 to 6 to choose an action:
   - **1**: Add a new employee (checks for valid name, role, and salary).
   - **2**: Edit an employee by ID (press Enter to keep old values).
   - **3**: Delete an employee by ID.
   - **4**: View a specific employee's details.
   - **5**: View the list of all employees.
   - **6**: View company stats and salary totals.
   - **0**: Exit the program safely.

[Software Demo Video](https://youtu.be/vzeNlcyGn8g)

# Relational Database

This project uses **SQLite** to manage data. The program automatically creates a database file named `directory.db` when it starts.

There is one table named **`employees`** with the following columns:

- **`id`**: Auto-incremented number to uniquely identify each person.
- **`name`**: Stores the employee's name.
- **`role`**: Stores the job title.
- **`salary`**: Stores the salary as a decimal number.

The program uses SQL aggregate functions to calculate company summaries in one query:

- `COUNT(*)` for total number of employees.
- `SUM(salary)` for the total budget.
- `AVG(salary)` for the average salary.
- `MAX(salary)` and `MIN(salary)` for the highest and lowest pay.

# Development Environment

Tools used to build this project:

- **IDE:** Visual Studio Code
- **Terminal:** Command Line to run the code
- **Database Tool:** SQLite Viewer extension

### Language and Libraries

The software is written in **Python 3** using only built-in libraries:

- **`sqlite3`**: To connect to the database and run SQL queries safely.
- **`locale`**: To automatically format the salary currency based on system settings.
- **`unittest`**: To automatically run tests and verify that adding, editing, and deleting data works correctly.

# Useful Websites

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Python Locale Documentation](https://docs.python.org/3/library/locale.html)
- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)

# Future Work

- **Import/Export to CSV:** Add options to download the employee list into a CSV file and upload new data from a CSV file.
- **Search by Name:** Add a feature to search for employees by typing their name instead of only searching by ID.
- **Multiple Tables:** Add a second table (like `departments`) and connect them using SQL `JOIN` queries.

import unittest
import database as db


### TEST DATABASE ###
class TestDatabase(unittest.TestCase):

    def test_db_crud(self):
        "Tests CRUD operations in the database"

        # 1. INITIALIZE DB
        db.initialize_db()

        # 2. CREATE (Insert data)
        original_name = "Test Employee"
        insert_result = db.add_employee(original_name, "Tester", 2500.00)
        self.assertTrue(insert_result, "Database Insert Failed")

        # 3. READ (Retrieve data)
        employees = db.get_all_employees()
        test_employee_id = None

        # Search for the created employee to get the ID
        for employee in employees:
            if employee[1] == original_name:
                test_employee_id = employee[0]
                break

        # Check if we found the employee
        self.assertIsNotNone(
            test_employee_id, "Employee has not been found in the database"
        )

        # 4. UPDATE (Modify data)
        updated_name = "Updated Employee"
        edit_result = db.edit_employee(
            test_employee_id, updated_name, "Senior Tester", 3500.00
        )
        self.assertTrue(edit_result, "Database Edit Failed")

        # Verify the update worked by retrieving the employee
        updated_employee_data = db.get_employee(test_employee_id)

        # Check that the list is not empty
        self.assertTrue(
            len(updated_employee_data) > 0, "Could not retrieve updated employee"
        )

        # Retrieve and check if the values changed
        updated_employee = updated_employee_data[0]
        self.assertEqual(updated_employee[1], updated_name, "Name was not updated")
        self.assertEqual(updated_employee[2], "Senior Tester", "Role was not updated")
        self.assertEqual(updated_employee[3], 3500.00, "Salary was not updated")

        # 5. DELETE (Remove data)
        delete_result = db.delete_employee(test_employee_id)
        self.assertTrue(delete_result, "Deletion from database has failed")

        # Verify the deletion worked
        deleted_employee_data = db.get_employee(test_employee_id)
        self.assertEqual(
            len(deleted_employee_data),
            0,
            "Employee was not deleted, it still exists",
        )


if __name__ == "__main__":
    unittest.main()

from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # Create
    emp = Employee(name="Alice", position="Manager", salary=75000, hire_date="2023-01-01")
    dao.insert(emp)
    print("Employee inserted.")

    # Read by ID
    employee = dao.get_by_id(1)
    print("Get by ID:", employee)

    # Read all
    all_employees = dao.get_all()
    print("All employees:")
    for emp in all_employees:
        print(emp)

    # Update
    if employee:
        employee.salary = 80000
        dao.update(employee)
        print("Updated employee:", dao.get_by_id(employee.id))

    # Delete
    dao.delete(1)
    print("Deleted employee with ID 1.")

if __name__ == "__main__":
    main()

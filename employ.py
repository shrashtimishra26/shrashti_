  import sqlite3


# ---------------- DATABASE ----------------

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (                       
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

conn.commit()


# ---------------- EMPLOYEE CLASS ----------------

class Employee:

    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def add_employee(self):
        cursor.execute(
            "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
            (self.__name, self.__department, self.__salary)
        )

        conn.commit()
        print("Employee added successfully!")


# ---------------- MANAGER CLASS ----------------

class Manager(Employee):

    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size


# ---------------- VIEW EMPLOYEES ----------------

def view_employees():

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    if len(employees) == 0:
        print("No employees found.")

    else:
        print("\n----- Employee Records -----")

        for employee in employees:
            print(
                "ID:", employee[0],
                "| Name:", employee[1],
                "| Department:", employee[2],
                "| Salary:", employee[3]
            )


# ---------------- UPDATE EMPLOYEE ----------------

def update_employee():

    employee_id = int(input("Enter Employee ID: "))

    name = input("Enter new name: ")
    department = input("Enter new department: ")
    salary = float(input("Enter new salary: "))

    cursor.execute("""
    UPDATE employees
    SET name = ?, department = ?, salary = ?
    WHERE id = ?
    """, (name, department, salary, employee_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee updated successfully!")
    else:
        print("Employee not found.")


# ---------------- DELETE EMPLOYEE ----------------

def delete_employee():

    employee_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")


# ---------------- MAIN PROGRAM ----------------

while True:

    print("\n==============================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter employee name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))

        employee = Employee(name, department, salary)
        employee.add_employee()

    elif choice == "2":

        view_employees()

    elif choice == "3":

        update_employee()

    elif choice == "4":

        delete_employee()

    elif choice == "5":

        print("Thank you!")
        break

    else:

        print("Invalid choice!")


conn.close() 
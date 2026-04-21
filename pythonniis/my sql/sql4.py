import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="root",
    database="employee"   
)

cursor = conn.cursor()
def insert_employee(emp_id, emp_name, emp_sal, emp_dept):
    query = "INSERT INTO employee (emp_id, emp_name, emp_sal, emp_dept) VALUES (%s, %s, %s, %s)"
    values = (emp_id, emp_name, emp_sal, emp_dept)
    cursor.execute(query, values)
    conn.commit()
    print("Employee inserted successfully!")
def display_employees():
    cursor.execute("SELECT * FROM employee")
    result = cursor.fetchall()
    
    print("\nEmployee Records:")
    for row in result:
        print(row)
def update_salary(emp_id, new_salary):
    query = "UPDATE employee SET emp_sal = %s WHERE emp_id = %s"
    cursor.execute(query, (new_salary, emp_id))
    conn.commit()
    print("Salary updated!")
def delete_employee(emp_id):
    query = "DELETE FROM employee WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    print("Employee deleted!")
while True:
    print("\n1. Insert Employee")
    print("2. Display Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        sal = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        insert_employee(emp_id, name, sal, dept)

    elif choice == 2:
        display_employees()

    elif choice == 3:
        emp_id = int(input("Enter ID: "))
        sal = float(input("Enter New Salary: "))
        update_salary(emp_id, sal)

    elif choice == 4:
        emp_id = int(input("Enter ID to delete: "))
        delete_employee(emp_id)

    elif choice == 5:
        break

    else:
        print("Invalid choice!")
conn.close()
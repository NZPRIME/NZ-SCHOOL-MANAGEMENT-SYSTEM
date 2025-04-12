import mysql.connector

# Database connection details (replace with your credentials)
db_host = "localhost"
db_user = "root"
db_password = "786Nawazish"
db_name = "student_db"

# Connect to the database
conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = conn.cursor()

# Function to add a new student
def add_student(name, roll_number, courses):
    sql = "INSERT INTO students (name, roll_number, courses) VALUES(%s, %s, %s)"
    data = (name, roll_number, courses)
    cursor.execute(sql, data)
    conn.commit()
    print("Student added successfully!")

# Function to update student details
def update_student(name, roll_number, new_name, new_roll_number, new_courses):
    sql = "UPDATE students SET name = %s, roll_number = %s, courses = %s WHERE roll_number = %s"
    data = (new_name, new_roll_number, new_courses, roll_number)
    cursor.execute(sql, data)
    conn.commit()
    print("Student updated successfully!")

# Function to delete a student
def delete_student(roll_number):
    sql = "DELETE FROM students WHERE roll_number = %s"
    data = (roll_number,)
    cursor.execute(sql, data)
    conn.commit()
    print("Student deleted successfully!")

# Function to display all students
def display_students():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    students = cursor.fetchall()
    if students:
        for student in students:
            print(f"ID: {student[0]} Name: {student[1]} Roll Number: {student[2]} Courses: {student[3]}")
    else:
        print("No students found!")

# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        courses = input("Enter comma-separated courses (optional): ")
        add_student(name, roll_number, courses)
    elif choice == '2':
        roll_number = input("Enter roll number of student to update: ")
        new_name = input("Enter new name (press Enter to skip): ")
        new_roll_number = input("Enter new roll number (press Enter to skip): ")
        new_courses = input("Enter new comma-separated courses (press Enter to skip): ")
        update_student(name, roll_number, new_name, new_roll_number, new_courses)
    elif choice == '3':
        roll_number = input("Enter roll number of student to delete: ")
        delete_student(roll_number)
    elif choice == '4':
        display_students()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection
cursor.close()
conn.close()

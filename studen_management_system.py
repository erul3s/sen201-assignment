students = []

def add_students():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    department = input("Enter department: ")

    student = {
        "name": name,
        "matric": matric,
        "department": department
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    for i, student in enumerate(students, start=1):
        print(f"Student {i}")
        print(f"Name: {student['name']}")
        print(f"Matric No: {student['matric']}")
        print(f"Department: {student['department']}")
        print("---------------------------")

def main_menu():
    while True:
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

# Start the program
main_menu()

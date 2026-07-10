
students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print(f"{name} added successfully!")

   
    elif choice == 2:
        search = input("Enter student name to search: ")

        if search in students:
            print(f"{search} is present in the list.")
        else:
            print(f"{search} is not found.")

   
    elif choice == 3:
        delete = input("Enter student name to delete: ")

        if delete in students:
            students.remove(delete)
            print(f"{delete} deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 4:
        if len(students) == 0:
            print("No students available.")
        else:
            print("\nStudent List:")
            for student in students:
                print(student)

   
    elif choice == 5:
        print("Thank you for using Student Management System!")
        break

   
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")



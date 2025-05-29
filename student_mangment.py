import os

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    try:
        marks1 = float(input("Enter marks for Subject 1: "))
        marks2 = float(input("Enter marks for Subject 2: "))
        marks3 = float(input("Enter marks for Subject 3: "))
    except ValueError:
        print("Please enter valid numbers for marks!")
        return

    total = marks1 + marks2 + marks3
    average = total / 3

    student = {
        "Name": name,
        "Roll No": roll,
        "Marks": [marks1, marks2, marks3],
        "Total": total,
        "Average": round(average, 2)
    }
    students.append(student)
    print("\nStudent added successfully!\n")

def display_students():
    if not students:
        print("\nNo student records available.\n")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['Name']}, Roll No: {s['Roll No']}, Marks: {s['Marks']}, Total: {s['Total']}, Average: {s['Average']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s['Roll No'] == roll:
            print(f"\nStudent Found: Name: {s['Name']}, Marks: {s['Marks']}, Total: {s['Total']}, Average: {s['Average']}\n")
            return
    print("\nStudent not found.\n")

def save_to_file():
    with open("student_records.txt", "w") as f:
        for s in students:
            f.write(f"{s['Name']},{s['Roll No']},{s['Marks'][0]},{s['Marks'][1]},{s['Marks'][2]},{s['Total']},{s['Average']}\n")
    print("\nRecords saved to student_records.txt\n")

def load_from_file():
    if not os.path.exists("student_records.txt"):
        print("\nNo file found to load records.\n")
        return
    with open("student_records.txt", "r") as f:
        for line in f:
            data = line.strip().split(',')
            student = {
                "Name": data[0],
                "Roll No": data[1],
                "Marks": [float(data[2]), float(data[3]), float(data[4])],
                "Total": float(data[5]),
                "Average": float(data[6])
            }
            students.append(student)
    print("\nRecords loaded successfully!\n")

def menu():
    while True:
        print("----- Student Result Management -----")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll No")
        print("4. Save Records to File")
        print("5. Load Records from File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            save_to_file()
        elif choice == '5':
            load_from_file()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

# Start the program
menu()

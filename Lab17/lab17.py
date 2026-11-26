# Lab 17 - Student Records Handling

# 2. Functions to Implement

def calc_total_average(marks):
    """Receives a list of marks. Calculates and returns total and average."""
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average


def display_student(roll_number, student):
    """Receives the roll number and student dictionary. Computes total and average,
    then prints a formatted line containing Roll Number, Name, Marks, Total, and Average."""
    name = student["name"]
    marks = student["marks"]
    total, average = calc_total_average(marks)
    print(f"Roll No: {roll_number} | Name: {name} | Marks: {marks} | Total: {total} | Average: {average:.2f}")


def add_student(students, roll_number, name, marks):
    """Receives the dictionary, roll number, name, and marks list.
    Checks if the roll number already exists. If yes, displays an error message.
    Otherwise, adds the student record and prints confirmation."""
    if roll_number in students:
        print(f"Error: Student with roll number {roll_number} already exists!")
    else:
        students[roll_number] = {
            "name": name,
            "marks": marks
        }
        print(f"Success: Student {name} added successfully!")


# 1. Data Setup & Prepopulation
students = {
    "101": {
        "name": "Alice",
        "marks": [85, 90, 78]
    },
    "102": {
        "name": "Bob",
        "marks": [92, 88, 95]
    }
}


# 3. Menu Operations (Continuous loop offering 4 menu-driven operations)
while True:
    print("\n--- Student Records Menu ---")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        # Choice 1: Display All Students
        if not students:
            print("No student records found.")
        else:
            for roll_no, student_info in students.items():
                display_student(roll_no, student_info)
                
    elif choice == "2":
        # Choice 2: Add New Student
        roll_no = input("Enter Roll Number: ").strip()
        name = input("Enter Name: ").strip()
        
        try:
            # Prompt for marks in 3 subjects and convert them to integers
            m1 = int(input("Enter marks for Subject 1: "))
            m2 = int(input("Enter marks for Subject 2: "))
            m3 = int(input("Enter marks for Subject 3: "))
            marks_list = [m1, m2, m3]
            
            add_student(students, roll_no, name, marks_list)
        except ValueError:
            print("Invalid input! Please enter integer values for marks.")
            
    elif choice == "3":
        # Choice 3: Search Student
        roll_no = input("Enter Roll Number to search: ").strip()
        student = students.get(roll_no)
        
        if student:
            display_student(roll_no, student)
        else:
            print(f"Error: Student with roll number {roll_no} not found.")
            
    elif choice == "4":
        # Choice 4: Exit
        print("Thank you for using Student Records Handling. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
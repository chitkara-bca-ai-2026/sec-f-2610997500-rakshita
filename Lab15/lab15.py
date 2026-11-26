# Header Banner
print("========================================")
print("  STUDENT INFORMATION MANAGEMENT SYSTEM")
print("========================================")

# 1. Initial Data Setup with default students
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [91, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

# 2. Interactive Loop
while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ").strip()
    
    # Choice 1: View All Students
    if choice == '1':
        print("\n--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']:<10} | Branch: {info['Branch']}")
            print(f" | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")
        
    # Choice 2: Search Student by Roll Number
    elif choice == '2':
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print(f"\n[ERROR] No record found for Roll No {roll}!")
            
    # Choice 3: Register New Student
    elif choice == '3':
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ").strip()
        
        if roll in students:
            print(f"\n[ERROR] Roll Number '{roll}' already exists!")
        else:
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch (e.g. BCA AI): ").strip()
            sem = input("Enter Semester: ").strip()
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))
            
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": sem,
                "Marks": [m1, m2, m3]
            }
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
            
    # Choice 4: Update Student Details
    elif choice == '4':
        roll = input("Enter Roll Number to update: ").strip()
        if roll in students:
            student = students[roll]
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            update_choice = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()
            
            if update_choice == '1':
                new_branch = input("Enter new branch: ").strip()
                student['Branch'] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif update_choice == '2':
                new_sem = input("Enter new semester: ").strip()
                student['Semester'] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid field selection!")
        else:
            print(f"[ERROR] Student with Roll No {roll} does not exist.")
            
    # Choice 5: View Academic Performance
    elif choice == '5':
        roll = input("Enter Roll Number for Academic Performance: ").strip()
        student = students.get(roll)
        if student:
            total = sum(student['Marks'])
            avg = total / len(student['Marks'])
            result = "PASS" if avg >= 40.0 else "FAIL"
            
            print("\n============== ACADEMIC REPORT ==============")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / {len(student['Marks']) * 100}")
            print(f"Average Marks: {avg:.2f}%")
            print(f"Final Result : {result}")
            print("=============================================")
        else:
            print(f"[ERROR] No record found for Roll No {roll}!")
            
    # Choice 6: Delete Student Record
    elif choice == '6':
        roll = input("Enter Roll Number to delete: ").strip()
        removed_student = students.pop(roll, None)
        if removed_student:
            print(f'\n[SUCCESS] Record for "{removed_student["Name"]}" (Roll No: {roll}) deleted successfully.')
        else:
            print(f'\n[ERROR] No record found for Roll No {roll}!')
            
    # Choice 7: Exit
    elif choice == '7':
        print("\nThank you for using Student Information System. Goodbye!")
        break
        
    else:
        print("\n[ERROR] Invalid choice! Please select a option between 1 and 7.")
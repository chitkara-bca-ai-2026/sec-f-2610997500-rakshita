import os

FILENAME = "notes.txt"

def write_notes(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print("Notes saved successfully.")

def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return "No notes file exists yet."

while True:
    print("\n1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        content = input("Enter your notes: ")
        write_notes(FILENAME, content)

    elif choice == "2":
        print("\n--- Saved Notes ---")
        print(read_notes(FILENAME))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 3.")
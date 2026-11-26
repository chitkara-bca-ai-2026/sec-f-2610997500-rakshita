# LAB 14 - LIBRARY BOOK & CATEGORY MANAGER

# 1. Initial Data Setup
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

# Create a set of unique library categories
library_categories = {book[3] for book in books}

# Student wishlist
student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}

# 2. Menu-driven program
while True:
    print("\n========================================")
    print("       LIBRARY BOOK & CATEGORY MANAGER")
    print("========================================")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    try:
        choice = int(input("\nEnter your choice (1-6): "))
    except ValueError:
        print("[ERROR] Please enter a valid number from 1 to 6.")
        continue

    if choice < 1 or choice > 6:
        print("[ERROR] Invalid choice! Please select between 1 and 6.")
        continue

    # Choice 1: View Books
    if choice == 1:
        print("\n--- Current Library Catalog (Fixed Records) ---")

        for i, (title, author, year, category) in enumerate(books, start=1):
            print(
                f'{i}. "{title}" by {author} ({year}) '
                f'| Genre: {category}'
            )

        print("Total Books:", len(books))

    # Choice 2: Add Book
    elif choice == 2:
        print("\n--- Add New Book Record ---")

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()

        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)

            print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("[ERROR] All fields are required. Book not added.")

    # Choice 3: View Categories
    elif choice == 3:
        print("\n--- Unique Categories Available in Library (Set) ---")

        for category in sorted(library_categories):
            print("-", category)

        print("Total Unique Genres:", len(library_categories))

    # Choice 4: Add Category to Wishlist
    elif choice == 4:
        print("\n--- Add to Student Wishlist ---")

        category = input("Enter requested category: ").strip()

        if category:
            student_wishlist.add(category)
            print(
                f'[SUCCESS] "{category}" added to student wishlist.'
            )
        else:
            print("[ERROR] Category cannot be empty.")

    # Choice 5: Category Gap Analysis
    elif choice == 5:
        print("\n================ CATEGORY GAP ANALYSIS ================")
        print("Library Holdings (Set):", sorted(library_categories))
        print("Student Wishlist (Set):", sorted(student_wishlist))

        # Intersection: Categories already available
        available = library_categories & student_wishlist

        # Difference: Categories requested but not available
        missing = student_wishlist - library_categories

        # Union: Complete combined genre coverage
        combined = library_categories | student_wishlist

        print("\n1. Already in Stock (Intersection &):")
        print(sorted(available))

        print("\n2. Purchase Order Needed (Difference -):")
        print(sorted(missing))

        print("\n3. Full Combined Genre Coverage (Union |):")
        print(sorted(combined))

        print("========================================================")

    # Choice 6: Exit
    elif choice == 6:
        print("\nThank you for using the Library Manager. Goodbye!")
        break
from library_system import LibrarySystem

my_library = LibrarySystem("HKMU Campus Library")

# UI for print library
def library_ui():
    print("="*50)
    print(f"Welcome to {my_library.get_library_info().split(',')[0]}")
    print("="*50)

    while True:
        # Display menu options
        print("\nMenu Options:")
        print("1. Add User/ Librarian")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. View User Details")
        print("7. View Library Info")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            
            # Add user or librarian
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            user_type = input("Enter User Type (Student/Librarian): ").capitalize()
            staff_id = input("Enter Staff ID (only for Librarian): ") if user_type == "Librarian" else None
            print(my_library.add_user(user_id, name, email, user_type, staff_id))

        elif choice == "2":
            # Add new book
            isbn = input("Enter 13-digit ISBN: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            genre = input("Enter Genre: ")
            available_copies = int(input("Enter Available Copies: "))
            print(my_library.add_book(isbn, title, author, genre, available_copies))

        elif choice == "3":
            # Borrow a book
            user_id = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            print(my_library.borrow_book(user_id, isbn))

        elif choice == "4":
            # Return a book
            user_id = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            print(my_library.return_book(user_id, isbn))

        elif choice == "5":
            # View all books
            print("\nAll Books in Library:")
            for book in my_library.get_all_books():
                print(book)
            
        elif choice == "6":
            # View user details
            user_id = input("Enter User ID: ")
            print(my_library.get_user_details(user_id))

        elif choice == "7":
            # View library statistics
            print(my_library.get_library_info())

        elif choice == "8":
            # Exit program
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice—please enter 1-8")

if __name__ == "__main__":
    # start UI
    library_ui()
from entities import Book, User, Librarian

# Main library
class LibrarySystem:
    def __init__(self, library_name):
        self._library_name = library_name
        self._books = {}  # ISBN -> Book mapping
        self._users = {}  # user_id -> User mapping
        self._librarians = {}  # staff_id -> Librarian mapping

    # Add a new user or librarian to the system
    def add_user(self, user_id, name, email, user_type="Student", staff_id=None):
        if user_id in self._users:
            return "User ID already exists"
        if user_type == "Librarian" and staff_id:
            # Use factory method for librarian creation
            librarian = Librarian.create_librarian(user_id, name, email, staff_id)
            self._users[user_id] = librarian
            self._librarians[staff_id] = librarian

            return f"Librarian {name} added successfully"
        else:
            user = User(user_id, name, email, user_type)
            self._users[user_id] = user

            return f"User {name} added successfully"

    # Add a new book - validates ISBN using static method
    def add_book(self, isbn, title, author, genre, available_copies):
        if not Book.is_valid_isbn(isbn):
            return "Invalid ISBN (must be 13 digits)"
        
        if isbn in self._books:
            return "Book ISBN already exists"
        
        book = Book(isbn, title, author, genre, available_copies)
        self._books[isbn] = book

        return f"Book {title} added successfully"

    # Handle book borrowing process
    def borrow_book(self, user_id, isbn):
        if user_id not in self._users:
            return "User not found"
        
        if isbn not in self._books:
            return "Book not found"
        
        user = self._users[user_id]
        book = self._books[isbn]
        result = book.borrow(user)

        if "Successfully borrowed" in result:
            user.add_borrowed_book(book)

        return result

    # Process book return
    def return_book(self, user_id, isbn):
        if user_id not in self._users or isbn not in self._books:
            return "User or Book not found"
        
        return self._books[isbn].return_item(self._users[user_id])

    # Return list of all books with their details
    def get_all_books(self):
        return [book.get_details() for book in self._books.values()]

    # Get detailed information about a user
    def get_user_details(self, user_id):
        if user_id in self._users:
            return self._users[user_id].get_details()
        return "User not found"

    # Get overall data
    def get_library_info(self):
        return f"Library Name: {self._library_name}, Total Books: {Book.total_books}, Total Users: {len(self._users)}, Total Librarians: {len(self._librarians)}"
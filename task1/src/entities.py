from abstract_classes import LibraryEntity, Borrowable
from datetime import datetime

# Book class
class Book(Borrowable):
    
    # total book
    total_books = 0

    def __init__(self, isbn, title, author, genre, available_copies):
        # Using protected attributes (encapsulation)
        self._isbn = isbn  
        self._title = title
        self._author = author
        self._genre = genre
        self._available_copies = available_copies
        self._borrowed_by = {}  # Track who borrowed and when
        Book.total_books += 1  

    # Getter methods - following formal OOP pattern
    def get_isbn(self):
        return self._isbn

    def get_available_copies(self):
        return self._available_copies

    # Setter method with validation
    def set_available_copies(self, num):
        if num >= 0:
            self._available_copies = num
        else:
            raise ValueError("Available copies cannot be negative")

    # Formal getter for details
    def get_details(self):
        return f"ISBN: {self._isbn}, Title: {self._title}, Author: {self._author}, Genre: {self._genre}, Available: {self._available_copies}"

    # real borrow action
    def borrow(self, user):
        if self._available_copies > 0:
            self._available_copies -= 1
            self._borrowed_by[user.get_user_id()] = datetime.now().strftime("%Y-%m-%d")
            return f"Successfully borrowed {self._title}"
        else:
            return f"No copies of {self._title} available"

    def return_item(self, user):
        user_id = user.get_user_id()
        if user_id in self._borrowed_by:
            self._available_copies += 1
            del self._borrowed_by[user_id]
            return f"Successfully returned {self._title}"
        else:
            return f"{user.get_name()} did not borrow {self._title}"

    # static func to valid isbn
    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()


# User entity - base class for students and librarians
class User(LibraryEntity):
    def __init__(self, user_id, name, email, user_type="Student"):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._user_type = user_type
        self._borrowed_books = []

    # Getter methods following formal pattern
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_details(self):
        return f"User ID: {self._user_id}, Name: {self._name}, Email: {self._email}, Type: {self._user_type}"

    
    def add_borrowed_book(self, book):
        #Track borrowed books by ISBN
        self._borrowed_books.append(book.get_isbn())


class Librarian(User):
    # Specialized User type with staff privileges
    def __init__(self, user_id, name, email, staff_id):
        # Call parent constructor with Librarian type
        super().__init__(user_id, name, email, user_type="Librarian")  
        self._staff_id = staff_id

    # Override get_details for librarian-specific info
    def get_details(self):
        return f"Librarian ID: {self._user_id}, Name: {self._name}, Staff ID: {self._staff_id}, Email: {self._email}"

    
    @classmethod
    def create_librarian(cls, user_id, name, email, staff_id):
        return cls(user_id, name, email, staff_id)
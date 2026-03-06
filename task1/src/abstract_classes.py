from abc import ABC, abstractmethod

# inhert ABC and define abstract func
class LibraryEntity(ABC):
    # Abstract base class for all library entities (books, users, etc.)
    @abstractmethod
    def get_details(self):
        pass

# Abstract Interface
class Borrowable(ABC):
    # borrow func
    @abstractmethod
    def borrow(self, user):
        pass

    # return func
    @abstractmethod
    def return_item(self, user):
        pass
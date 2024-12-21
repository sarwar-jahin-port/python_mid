# Create the library class
class Library:
    _book_list = []

    @classmethod
    def entry_book(cls, book):
        cls._book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability) -> None:
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)
    
    def view_book_info(self):
        print(f"ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Availability: {self.__availability}")

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"{self.__title} is available. Here it is.")
        else:
            print(f"The {self.__title} is not available right now")
    
    def return_book(self):
        if not self.__availability:    
            self.__availability = True
            print(f"Thanks for returning the book")
        else:
            print(f"{self.__title} is not our book")

    def get_book_id(self):
        return self.__book_id
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_availability(self):
        return self.__availability

lib = Library()
book1 = Book(1, "Python with Phitron", "Sarwar", True)
book2 = Book(2, "DSA with Phitron", "Jahin", True)
book3 = Book(3, "C programming with Phitron", "Rahat vai", True)

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All books")
        print("2. Borrow book")
        print("3. Return book")
        print("4. Exit")

        choice = input("Enter your choice(1/ 2 / 3/ 4): ")

        if choice == '1':
            print("\nAll books in the library: ")
            for book in lib._book_list:
                book.view_book_info()
                print()
        elif choice == '2':
            book_id = int(input("Enter the book ID to borrow: "))
            found = False

            for book in lib._book_list:
                if book.get_book_id() == book_id:
                    book.borrow_book()
                    found = True
                    break
            if not found:
                print("Book not found")
        elif choice == '3':
            book_id = int(input("Enter the book id to return: "))
            found = False
            for book in lib._book_list:
                if book.get_book_id() == book_id:
                    book.return_book()
                    found = True
                    break
            if not found:
                print("Book not found")
        elif choice == '4':
            print("Leaving the library....")
            break
        else:
            print("Invalid choice, please try again")
menu()
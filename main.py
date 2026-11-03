"""
Library Management System - Python OOP mini project
Concepts: classes, objects, encapsulation, inheritance, polymorphism, composition.
Run with: python main.py
"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"{self.book_id} | {self.title} | {self.author} | {status}")


class Member:
    def __init__(self, member_id, name):
        self._member_id = member_id
        self._name = name
        self._borrowed_books = []

    @property
    def member_id(self):
        return self._member_id

    @property
    def name(self):
        return self._name

    def get_member_type(self):
        return "Regular Member"

    def display(self):
        print(f"{self.member_id} | {self.name} | {self.get_member_type()} | "
              f"Borrowed: {len(self._borrowed_books)}")


class StudentMember(Member):
    def get_member_type(self):
        return "Student Member"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
            return
        self.books[book.book_id] = book
        print("Book added.")

    def register_member(self, member):
        if member.member_id in self.members:
            print("Member ID already exists.")
            return
        self.members[member.member_id] = member
        print("Member registered.")

    def show_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books.values():
            book.display()

    def show_members(self):
        if not self.members:
            print("No members registered.")
        for member in self.members.values():
            member.display()

    def search_books(self, keyword):
        found = False
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                book.display()
                found = True
        if not found:
            print("No matching books found.")

    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if book is None or member is None:
            print("Invalid book ID or member ID.")
        elif not book.is_available:
            print("Book is already issued.")
        else:
            book.is_available = False
            member._borrowed_books.append(book_id)
            print(f'"{book.title}" issued to {member.name}.')

    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if book is None or member is None:
            print("Invalid book ID or member ID.")
        elif book_id not in member._borrowed_books:
            print("This member has not borrowed that book.")
        else:
            member._borrowed_books.remove(book_id)
            book.is_available = True
            print("Book returned successfully.")


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    library = Library()
    library.add_book(Book(101, "The Alchemist", "Paulo Coelho"))
    library.add_book(Book(102, "Wings of Fire", "A. P. J. Abdul Kalam"))
    library.add_book(Book(103, "Python Crash Course", "Eric Matthes"))
    library.register_member(StudentMember(1, "Aarav"))
    library.register_member(Member(2, "Maya"))

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. View books")
        print("2. Search books")
        print("3. View members")
        print("4. Register member")
        print("5. Add book")
        print("6. Issue book")
        print("7. Return book")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.show_books()
        elif choice == "2":
            library.search_books(input("Enter title/author keyword: ").strip())
        elif choice == "3":
            library.show_members()
        elif choice == "4":
            member_id = get_int("Member ID: ")
            if member_id is not None:
                name = input("Member name: ").strip()
                if name:
                    library.register_member(Member(member_id, name))
                else:
                    print("Name cannot be empty.")
        elif choice == "5":
            book_id = get_int("Book ID: ")
            if book_id is not None:
                title = input("Book title: ").strip()
                author = input("Author: ").strip()
                if title and author:
                    library.add_book(Book(book_id, title, author))
                else:
                    print("Title and author cannot be empty.")
        elif choice == "6":
            book_id = get_int("Book ID: ")
            member_id = get_int("Member ID: ")
            if book_id is not None and member_id is not None:
                library.issue_book(book_id, member_id)
        elif choice == "7":
            book_id = get_int("Book ID: ")
            member_id = get_int("Member ID: ")
            if book_id is not None and member_id is not None:
                library.return_book(book_id, member_id)
        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

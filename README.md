# Library Management System - Python OOP

A menu-driven command-line project demonstrating Object-Oriented Programming in Python.

## Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run `python main.py`.

## Features
- View and search books by title or author.
- Register members.
- Add books.
- Issue available books to members.
- Return borrowed books.
- Check book availability.

## OOP concepts
- **Classes and objects:** `Book`, `Member`, `StudentMember`, `Library`.
- **Encapsulation:** Member details are kept in underscored attributes and exposed through properties.
- **Inheritance:** `StudentMember` inherits from `Member`.
- **Polymorphism:** `StudentMember` overrides `get_member_type()`.
- **Composition:** `Library` stores and manages Book and Member objects.

## Sample records
The program starts with three books and two members to make testing easy.

## Test the program
1. Select `1` to view books.
2. Select `6`, enter book ID `103` and member ID `1` to issue *Python Crash Course*.
3. Select `1` to see its status change to Issued.
4. Select `7`, enter book ID `103` and member ID `1` to return it.

## Files
- `main.py` - complete Python program.
- `README.md` - project documentation.

## Future enhancements
Records can be saved in a database, and due dates, fine calculation, login, or a GUI can be added.

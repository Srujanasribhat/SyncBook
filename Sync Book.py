# -----------------------------
# Book Class
# -----------------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.book_id} | {self.title} | {self.author} | {status}")


# -----------------------------
# Member Class
# -----------------------------
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self._borrowed_books = []      # Encapsulation

    def borrow(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        self._borrowed_books.remove(book)

    def show_books(self):
        print(f"\nBooks borrowed by {self.name}:")
        if len(self._borrowed_books) == 0:
            print("No books borrowed.")
        else:
            for b in self._borrowed_books:
                print("-", b.title)


# -----------------------------
# Inheritance
# -----------------------------
class StudentMember(Member):
    def __init__(self, member_id, name, course):
        super().__init__(member_id, name)
        self.course = course


# -----------------------------
# Library Class (Composition)
# -----------------------------
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)

    # Add Member
    def add_member(self, member):
        self.members.append(member)

    # Search Book
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display()
                return book
        print("Book not found.")
        return None

    # Borrow Book
    def borrow_book(self, member_id, title):

        member = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            print("Member not found.")
            return

        book = self.search_book(title)

        if book is not None:
            if book.available:
                book.available = False
                member.borrow(book)
                print(f"{member.name} borrowed '{book.title}'")
            else:
                print("Book already borrowed.")

    # Return Book
    def return_book(self, member_id, title):

        member = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            print("Member not found.")
            return

        for book in member._borrowed_books:
            if book.title.lower() == title.lower():
                member.return_book(book)
                book.available = True
                print(f"{member.name} returned '{book.title}'")
                return

        print("Book not borrowed.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books")
        print("-" * 40)
        for book in self.books:
            book.display()


# -----------------------------
# Main Program
# -----------------------------
library = Library()

# Add Books
library.add_book(Book(101, "Python Basics", "Guido"))
library.add_book(Book(102, "Data Structures", "Mark"))
library.add_book(Book(103, "Machine Learning", "Andrew"))

# Add Members
library.add_member(StudentMember(1, "Alice", "CSE"))
library.add_member(StudentMember(2, "Bob", "ECE"))

while True:

    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Display Books")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Member Books")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        library.display_books()

    elif choice == 2:
        title = input("Enter Book Title: ")
        library.search_book(title)

    elif choice == 3:
        member = int(input("Member ID: "))
        title = input("Book Title: ")
        library.borrow_book(member, title)

    elif choice == 4:
        member = int(input("Member ID: "))
        title = input("Book Title: ")
        library.return_book(member, title)

    elif choice == 5:
        member = int(input("Member ID: "))
        found = False

        for m in library.members:
            if m.member_id == member:
                m.show_books()
                found = True

        if not found:
            print("Member not found.")

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
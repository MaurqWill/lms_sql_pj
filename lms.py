
# Main Menu:
# 1. Book Operations
# 2. User Operations
# 3. Author Operations
# 4. Quit

# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books

# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users

# Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors

main_menu = """
Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Make a selection: """

book_operations_menu = """
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books

Make a selection: """

user_operartions_menu = """
User Operations:
1. Add a new user
2. View user details
3. Display all users

Make a selection: """

author_operations_menu = """
Author Operations:
1. Add a new author
2. View author details
3. Display all authors

Make a selection: """

class Book: 
    def __init__(self, title, author, ISBN, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.is_available = True
    
    def check_out(self):
        if self.is_available:
            print(f"You successfully checked out {self.title}")
            self.is_available = False
            return True
        print(f"{self.title} is not available")
        return False
    
    def return_book(self):
        self.is_available = True

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_out():
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print("You haven't borrowed this book.")

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, library_id):
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"User {new_user.name} with ID {new_user.library_id} has been added.")

    def display_all_users(self):
        print("All Users:")
        for user in self.users:
            print(user.name, user.library_id, user.borrowed_books)

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def __str__(self):
        return f"Name: {self.name}\nBiography: {self.biography}"
    
    def add_author(self, name, biography):
        new_author = Author(name, biography)
        return new_author
    

class Library:
    def __init__(self):
        self.books = []
        self.user_manager = UserManager()

    def add_book(self):
        title = input("Enter book title: ")
        author_name = input("Enter author: ")
        ISBN = input("Enter ISBN: ")
        publication_date = input("Enter publication date: ")
        author = Author(author_name)  # Create a new Author instance with only the name
        self.authors.append(author)  # Add the new Author to the list of authors

        new_book = Book(title, author, ISBN, publication_date)
        self.books.append(new_book)
        print(f"{new_book.title} has been added to the library.")

    def borrow_book(self, title):
        book = self.book_search(title)
        if book:
            book.check_out()
        else:
            print(f"{title} not found in the library.")

    def book_search(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def return_book(self, title):
        book = self.book_search(title)
        if book:
            book.return_book()
            print(f"{title} has been returned.")
        else:
            print(f"{title} not found in the library.")

    def display_all_books(self):
        print("Here are all the books in the library: ")
        for book in self.books:
            print(book.title)

def lms():
    library = Library()
    while True:
        try:
            user_choice = input(main_menu).strip()

            if user_choice == '1':
                book_operations(library)
            elif user_choice == '2':
                user_operations(library)
            elif user_choice == '3':
                author_operations()
            elif user_choice == '4':
                break
            else:
                print("Invalid selection, try again.")

        except Exception as e:
            print("Error occurred:", e)
            print("Invalid selection, try again.")
        finally:
            print("Thank you for using the Library Management System! Until next time!")

def book_operations(library):
    while True:
        user_selection = input(book_operations_menu).strip()
        if user_selection == '1':
            library.add_book()
        elif user_selection == '2':
            library.borrow_book(input("Enter the title of the book to borrow: "))
        elif user_selection == '3':
            library.return_book(input("Enter the title of the book to return: "))
        elif user_selection == '4':
            title = input("Enter the title of the book to search: ")
            book = library.book_search(title)
            if book:
                print(f"{book.title} by {book.author} (ISBN: {book.ISBN}, Published: {book.publication_date})")
                if book.is_available:
                    print("Status: Available")
                else:
                    print("Status: Not Available")
            else:
                print(f"{title} not found in the library.")
        elif user_selection == '5':
            library.display_all_books()
        else:
            print("Invalid selection, try again.")

def user_operations(library):
    while True:
        user_selection = input(user_operartions_menu).strip()
        if user_selection == '1':
            name = input("Enter user's name: ").strip()
            library_id = input("Enter user's library ID: ").strip()
            library.user_manager.add_user(name, library_id)
        elif user_selection == '2':
            library.user_manager.display_all_users()
        elif user_selection == '3':
            library.user_manager.display_all_users()
            pass
        else:
            print("Invalid selection, try again.")

def author_operations(library):
    while True:
        user_pick = input(author_operations_menu).strip()
        if user_pick == '1':
            name = input("Enter author's name: ")
            biography = input("Enter author's biography: ")
            new_author = Author(name, biography)
            library.authors.append(new_author)
            print(f"Author {new_author.name} has been added.")
        elif user_pick == '2':
            print("Authors:")
            for author in library.authors:
                print(author)
        elif user_pick == '3':
            print("Authors:")
            for author in library.authors:
                print(author)
            
        else:
            print("Invalid selection, try again.")

lms()

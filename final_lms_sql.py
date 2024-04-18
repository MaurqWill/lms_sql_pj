from datetime import datetime
from connect_db import connect_db, Error
import mysql.connector
from mysql.connector import Error

class Library:
    def __init__(self, db_connection, cursor):
        self.db_connection = db_connection
        self.cursor = cursor

    def add_book(self):
        title = input("Enter book title: ")
        author_name = input("Enter author: ")
        ISBN = input("Enter ISBN: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")

        author_id = self.get_or_add_author(author_name)

        query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
        values = (title, author_id, ISBN, publication_date)
        self.cursor.execute(query, values)
        self.db_connection.commit()

        print(f"{title} has been added to the library.")

    def borrow_book(self):
        title = input("Enter the title of the book to borrow: ")

        query = "SELECT id, availability FROM books WHERE title = %s"
        self.cursor.execute(query, (title,))
        book = self.cursor.fetchone()

        if book:
            book_id, availability = book
            if availability:
                user_id = input("Enter user ID: ")

                borrow_date = datetime.today().strftime('%Y-%m-%d')
                query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                values = (user_id, book_id, borrow_date)
                self.cursor.execute(query, values)
                self.db_connection.commit()

                query = "UPDATE books SET availability = 0 WHERE id = %s"
                self.cursor.execute(query, (book_id,))
                self.db_connection.commit()

                print(f"{title} has been borrowed.")
            else:
                print(f"{title} is not available for borrowing.")
        else:
            print(f"{title} not found in the library.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")

        query = "SELECT id, availability FROM books WHERE title = %s"
        self.cursor.execute(query, (title,))
        book = self.cursor.fetchone()

        if book:
            book_id, availability = book
            if not availability:
                user_id = input("Enter user ID: ")

                return_date = datetime.today().strftime('%Y-%m-%d')
                query = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND user_id = %s AND return_date IS NULL"
                values = (return_date, book_id, user_id)
                self.cursor.execute(query, values)
                self.db_connection.commit()

                query = "UPDATE books SET availability = 1 WHERE id = %s"
                self.cursor.execute(query, (book_id,))
                self.db_connection.commit()

                print(f"{title} has been returned.")
            else:
                print(f"{title} is not borrowed.")
        else:
            print(f"{title} not found in the library.")

    def display_all_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        print("All Books:")
        for book in books:
            print(book)

    def add_user(self):
        name = input("Enter user's name: ")
        library_id = input("Enter user's library ID: ")

        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        values = (name, library_id)
        self.cursor.execute(query, values)
        self.db_connection.commit()

        print(f"User {name} with ID {library_id} has been added.")

    def display_all_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        users = self.cursor.fetchall()

        print("All Users:")
        for user in users:
            print(user)

    def add_author(self, name):
        
        query = "INSERT INTO authors (name) VALUES (%s)"
        values = (name,)
        self.cursor.execute(query, values)
        self.db_connection.commit()

        print(f"Author {name} has been added.")

    def display_all_authors(self):
        query = "SELECT * FROM authors"
        self.cursor.execute(query)
        authors = self.cursor.fetchall()

        print("All Authors:")
        for author in authors:
            print(author)

    def get_or_add_author(self, name):

        query = "SELECT id FROM authors WHERE name = %s"
        self.cursor.execute(query, (name,))
        author = self.cursor.fetchone()

        if author:
            return author[0]
        else:
            self.add_author(name)
            return self.cursor.lastrowid  

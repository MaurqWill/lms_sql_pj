CREATE DATABASE library_management_system;

USE library_management_system;

CREATE TABLE authors (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);


INSERT INTO authors (name, biography) 
VALUES ('J.R.R. Tolkien', 'John Ronald Reuel Tolkien was an English writer, poet, philologist, and academic, best known as the author of the classic high fantasy works The Hobbit, The Lord of the Rings, and The Silmarillion.');


INSERT INTO authors (name, biography) 
VALUES ('Agatha Christie', 'Agatha Mary Clarissa Christie, Lady Mallowan, was an English writer known for her sixty-six detective novels and fourteen short story collections, particularly those revolving around fictional detectives Hercule Poirot and Miss Marple.');


INSERT INTO authors (name, biography) 
VALUES ('Ernest Hemingway', 'Ernest Miller Hemingway was an American novelist, short-story writer, journalist, and sportsman. His economical and understated style—which he termed the iceberg theory—had a strong influence on 20th-century fiction.');


INSERT INTO users (name, library_id) 
VALUES ('John Smith', 'JS1234');


INSERT INTO users (name, library_id) 
VALUES ('Emily Johnson', 'EJ5678');


INSERT INTO users (name, library_id) 
VALUES ('Michael Brown', 'MB9012');


INSERT INTO books (title, author_id, isbn, publication_date) 
VALUES ('The Lord of the Rings', 1, '9780261103252', '1954-07-29');


INSERT INTO books (title, author_id, isbn, publication_date) 
VALUES ('And Then There Were None', 2, '9780062073488', '1939-11-06');



INSERT INTO books (title, author_id, isbn, publication_date) 
VALUES ('For Whom the Bell Tolls', 3, '9780684803357', '1940-10-21');

SELECT *
FROM authors;

SELECT *
FROM users;

SELECT *
FROM books;
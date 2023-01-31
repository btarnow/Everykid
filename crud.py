"""CRUD operations."""

# From model.py import all classes and connect_to_db function 
from model import db, Book, Author, Character, User, Rating_and_Review, Collection, connect_to_db


def create_book(book_id, isbn_13, title, year_published, cover_path, overview):
    """Create and return a new book."""

    book = Book(book_id = book_id, isbn_13 = isbn_13, title = title, 
                year_published = year_published, cover_path = cover_path, 
                overview = overview)

    return book


def add_author(book_id, author_name):
    """Create and return an author of a book"""

    # with author_id = author_id, we're strictly defining the variable to Python
    # If they weren't strictly defined, they could be accidentally put in any order 
    # as the parameters. 
    author = Author(book_id = book_id, author_name = author_name)

    return author 


def add_character(book_id, racial_identity, gender_identity):
    """Create and return a character in a book"""

    character = Character(book_id = book_id, racial_identity = racial_identity, 
                          gender_identity = gender_identity)

    return character
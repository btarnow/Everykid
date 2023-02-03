"""CRUD operations."""

# From model.py import all classes and connect_to_db function 
from model import db, Book, Author, Character, User, Rating_and_Review, Collection, connect_to_db


def create_book(book_id, isbn_13, title, year_published, cover_path, overview):
    """Create and return a new book."""

    book = Book(book_id = book_id, isbn_13 = isbn_13, title = title, 
                year_published = year_published, cover_path = cover_path, 
                overview = overview)

    return book


def create_author(book_id, author_name):
    """Create and return an author of a book"""

    # with author_id = author_id, we're strictly defining the variable to Python
    # If they weren't strictly defined, they could be accidentally put in any order 
    # as the parameters. 
    author = Author(book_id = book_id, author_name = author_name)

    return author 


def create_character(book_id, gender_identity, racial_identity):
    """Create and return a character in a book"""

    character = Character(book_id = book_id, racial_identity = racial_identity, 
                          gender_identity = gender_identity)

    return character



# write a CRUD function that takes in a race and gender identity and returns 
# all of the characters that meet that criteria  

def filter_characters(race_filter, gender_filter):
    """Filter books by a character's race and/or gender"""

    # Need to do a sqlalchemy query within the characters table.
    # To use make an AND statement in SQLalchemy, the syntax looks like this: 
    # Employee.query.filter( (Employee.state == 'CA') & (Employee.salary > 70000) )

    filtered_characters = Character.query.filter( (Character.racial_identity == 
                                              race_filter) & 
                                              (Character.gender_identity == 
                                               gender_filter) ).all()

    return filtered_characters


#TODO: 
# steps for later: 
# add a blank option to dropdowns 
# then modify crud filter_characters --> if else for gender/race filter both, 
# one or the other 


    

    

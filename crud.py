"""CRUD operations."""

from model import db, Book, Author, Character, User, Rating_and_Review, Collection, connect_to_db


def create_book(book_id, isbn_13, title, year_published, cover_path, overview):
    """Create and return a new book."""

    book = Book(book_id=book_id, isbn_13=isbn_13, title=title, 
                year_published=year_published, cover_path=cover_path, 
                overview=overview)

    return book


def create_author(book_id, author_name):
    """Create and return an author of a book"""

    author = Author(book_id=book_id, author_name=author_name)

    return author 


def create_character(book_id, gender_identity, racial_identity):
    """Create and return a character in a book"""

    character = Character(book_id=book_id, racial_identity=racial_identity, 
                          gender_identity=gender_identity)

    return character


def filter_characters(race_filter, gender_filter):
    """Filter books by a character's race and/or gender"""

    if race_filter == "ALL RACES" and gender_filter== "ALL GENDERS":
        filtered_characters = Character.query.all()
    
    elif gender_filter == "ALL GENDERS":
        filtered_characters = Character.query.filter(Character.racial_identity 
                                                     == race_filter).all()

    elif race_filter == "ALL RACES":
        filtered_characters = Character.query.filter(Character.gender_identity 
                                                     == gender_filter).all()
        
    else: 
        filtered_characters = Character.query.filter( (Character.racial_identity 
                                                       == race_filter) & 
                                                (Character.gender_identity == 
                                                gender_filter) ).all()

    return filtered_characters


def get_book_by_id(book_id):
    """Returns book by specific book_id"""

    return Book.query.get(book_id)


def find_similar_race_characters(char_race):
    """Find characters of all genders given a specific race"""
    
    similar_race_characters = Character.query.filter(Character.racial_identity == 
                                                char_race).all()
    
    return similar_race_characters


def find_similar_gender_characters(char_gender):
     """Find characters of all races given a specific gender"""

     similar_gender_characters = Character.query.filter(Character.gender_identity 
                                                        == char_gender).all()
     
     return similar_gender_characters
    

    

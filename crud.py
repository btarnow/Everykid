"""CRUD operations."""

from model import db, Book, Author, Character, User, Rating_and_Review, Collection, connect_to_db
# from passlib.hash import argon2


# ----- FUNCTIONS FOR BOOKS TABLE ----- #
def create_book(book_id, isbn_13, title, year_published, cover_path, overview):
    """Create and return a new book."""

    book = Book(book_id=book_id, isbn_13=isbn_13, title=title, 
                year_published=year_published, cover_path=cover_path, 
                overview=overview)

    return book


def get_book_by_id(book_id):
    """Returns book by specific book_id"""

    return Book.query.get(book_id)


# ----- FUNCTION FOR AUTHORS TABLE ----- #
def create_author(book_id, author_name):
    """Create and return an author of a book"""

    author = Author(book_id=book_id, author_name=author_name)

    return author 


# ----- FUNCTIONS FOR CHARACTERS TABLE ----- #
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


# ----- FUNCTIONS FOR USERS TABLE ----- #
def create_user(email, password, fname, lname):
    """Create and return a new user"""

    user = User(email=email, password=password, fname=fname, lname=lname)

    return user 


def get_user_by_email(email):
    """Return a user's info by email, else returns None"""

    return User.query.filter(User.email == email).first()


def get_user_by_id(user_id):
    """Return a user's info by user ID, else returns None"""

    return User.query.get(user_id)


def get_user_collections(user_id):
    """Return a list of user collections"""

    user = User.query.get(user_id)

    return user.collections


def get_all_users():
    """Return a list of all users"""

    return User.query.all()


# TODO: Change this this FUNCTIONS if more than one... 
# ----- FUNCTION FOR COLLECTIONS TABLE ----- #
def add_book_to_collection(user_id, book_id, collection_name):
    """Add a book to the collection"""

    book_to_add = Collection(user_id=user_id, book_id=book_id, 
                            collection_name=collection_name)
    
    return book_to_add

def create_collection(user_id, collection_name):
    """Create a collection"""

    collection = Collection(user_id=user_id, collection_name=collection_name)

    return collection 









    

    

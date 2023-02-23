"""CRUD operations."""

from model import db, Book, Author, Character, User, Collection, connect_to_db, Assoc_book_collection

# from sqlalchemy import delete


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


def get_all_users():
    """Return a list of all users"""

    return User.query.all()


# ----- FUNCTIONS FOR COLLECTIONS ----- #
def create_collection(user_id, collection_name):
    """Create a collection"""

    collection = Collection(user_id=user_id, collection_name=collection_name)

    return collection 


def add_book_to_collection(book_id, collection_id):
    """Creates a association object between a book and a collection"""

    book_to_collection = Assoc_book_collection(book_id=book_id, 
                                            collection_id=collection_id)
    
    return book_to_collection


def delete_book_from_collection(book_id, collection_id):
    """Find all books in a given collection to delete"""

    book_to_delete = Assoc_book_collection.query.filter_by(book_id=book_id, 
                                            collection_id=collection_id).first()

    return book_to_delete


def get_users_mybooks_collection(user_id):
    """Return the "My Books" collections for a user"""

    user = User.query.get(user_id)

    return user.collections[0]


def check_if_book_in_collection(book_id, collection_id):
    """Returns book if it's in the database, else returns None"""

    book_in_db = Assoc_book_collection.query.filter(Assoc_book_collection.book_id 
                                                    == book_id, 
                                                    Assoc_book_collection.collection_id 
                                                    == collection_id).first()
    
    return book_in_db



    










if __name__ == "__main__":
    from server import app
    connect_to_db(app)


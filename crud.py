"""CRUD operations."""

# From model.py import all classes and connect_to_db function 
from model import db, Book, Author, Character, User, Rating_and_Review, Collection, connect_to_db


def create_book(book_id, isbn_13, title, year_published, cover_path, overview):
    """Create and return a new book."""

    book = Book(book_id=book_id, isbn_13=isbn_13, title=title, 
                year_published=year_published, cover_path=cover_path, 
                overview=overview)

    return book


def create_author(book_id, author_name):
    """Create and return an author of a book"""

    # with author_id = author_id, we're strictly defining the variable to Python
    # If they weren't strictly defined, they could be accidentally put in any order 
    # as the parameters. 
    author = Author(book_id=book_id, author_name=author_name)

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
    ############################################################################
    
    # if the user selects 'ALL GENDERS' and 'ALL RACES': 
    if race_filter == "ALL RACES" and gender_filter== "ALL GENDERS":
        filtered_characters = Character.query.all()
    
   
    # if the user selects an individual race and 'ALL GENDERS': 
    elif gender_filter == "ALL GENDERS":
        filtered_characters = Character.query.filter(Character.racial_identity == 
                                                race_filter).all()

    # if the user selects an individual gender and 'ALL RACES': 
    elif race_filter == "ALL RACES":
        filtered_characters = Character.query.filter(Character.gender_identity == 
                                                gender_filter).all()
        

    # If the user selects an individual race and gender (aka NOT 'ALL RACES' or 
    # 'ALL GENDERS'): 
    else: 
        filtered_characters = Character.query.filter( (Character.racial_identity == 
                                                race_filter) & 
                                                (Character.gender_identity == 
                                                gender_filter) ).all()

    return filtered_characters


def get_book_by_id(book_id):
    """Returns book by specific book_id"""

    return Book.query.get(book_id)



### FOR PERSONALIZED RECOMMENDATIONS: 

# create a crud function to create a list of 
    # if the book is already displayed, DONT display this 

#create function to get a list of all cisgender female main characters  in crud 
# > in server use the crud function and use random generator to pick 5 book 
# titles > if book_title == display_book use the rand function to choose a new title



#TODO: 
# steps for later: 
# add a blank option to dropdowns 
# then modify crud filter_characters --> if else for gender/race filter both, 
# one or the other 


    

    

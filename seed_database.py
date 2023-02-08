"""Script to seed database"""

import os
import json
import crud 
import model
from server import app

os.system("dropdb books_db")
os.system("createdb books_db")

# Prevents error: 
app.app_context().push() 

model.connect_to_db(app)
model.db.create_all()

with open('static/books_database.json') as file:
    book_data = json.loads(file.read())


def seed_books():
    """This function iterates through books_database.json and creates an 
    instantiation of a book object that matches the required fields of the 
    columns in the model.py tables."""
    
    for key in book_data.keys():
        book_id = key
        isbn_13 = book_data[key]["isbn_13"]
        title = book_data[key]["title"]
        year_published = book_data[key]["year_published"]
        cover_path = book_data[key]["Cover Path"]
        overview = book_data[key]["overview"]

        book_to_add = crud.create_book(book_id, isbn_13, title, year_published, 
                                       cover_path, overview)
        
        model.db.session.add(book_to_add)


def seed_characters():
    """This function iterates through books_database.json and creates an 
    instantiation of a character object that matches the required fields of the 
    columns in the model.py tables."""

    for key in book_data.keys():
        book_id = key
        gender_identity = book_data[key]["gender_identity"]
        racial_identity = book_data[key]["racial_identity"]
        # For future versions, I would like to change the database to include a 
        # list of characters to allow books to include more than one character. 

        character_to_add = crud.create_character(book_id, gender_identity, 
                                              racial_identity)
        model.db.session.add(character_to_add)

        
def seed_authors():
    """This function iterates through books_database.json and creates an 
    instantiation of an author object that matches the required fields of the 
    columns in the model.py tables."""

    for key in book_data.keys():
        book_id = key
        author_name = book_data[key]["author_name"]
        for author in author_name:
            author_to_add = crud.create_author(book_id, author)
            model.db.session.add(author_to_add)

def seed_database():
    """Run all seed functions to seed database """
    seed_books()
    seed_characters()
    seed_authors()
    model.db.session.commit() 
    print("All seed functions ran.")

seed_database()


# To Test that these functions are working correctly, execute the following 
# in the command line: pg_dump books_db > books_practice.sql







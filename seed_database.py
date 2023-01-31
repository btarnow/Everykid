"""Script to seed database"""

import requests 
import os
import json
import crud 
import model
from server import app

# Whatever I put in as a parameter, it will execute in the command line:
# So instead of dropping and creating the database every time, I can instead run
# python3 seed_database.py and it will run the following commands: 
os.system("dropdb books_db")
os.system("createdb books_db")

# Prevents error: 
app.app_context().push() 

# Connecting to database 
model.connect_to_db(app)

# Creates tables 
model.db.create_all()

book_OLIDs_list = ["OL20914137W", "OL25074818W", "OL22020948W", "OL27139917W",
                   "OL26585018W", "OL21183636W", "OL19635091W", "OL20639677W", 
                   "OL27137338W", "OL20531661W", "OL25070735W", "OL39666203M", 
                   "OL24141019W", "OL20660371W", "OL46525616M", "OL24348919W", 
                   "OL46525603M", "OL19406W", "OL19987787W", "OL26886570M", 
                   "OL20055629W", "OL20128080W", "OL20128080W", "OL34975354M", 
                   "OL29531064M", "OL19743931W", "OL46525609M", "OL25873929W", 
                   "OL24327244W", "OL46525611M", "OL46525610M", "OL21874814W", 
                   "OL28716700M", "OL35289538M", "OL19667684W", "OL17072538M", 
                   "OL26977532M", "OL36181966M", "OL28091302M", "OL31807898M", 
                   "OL20984012W", "OL20568318W", "OL27911917M", "OL12312396M"]


def create_database(book_OLIDs_list):
    """This function pulls data from the Open Library API to seed the database"""

    books_database = {}

    for book_OLID in book_OLIDs_list:
        ind_book_dict = {}
        book_request = requests.get(f"https://openlibrary.org/works/{book_OLID}.json")
        book_data = book_request.json()

        # Get Title:
        title = book_data.get("title", "No title found")
        ind_book_dict["title"] = title


        # Get Publish Date: 
        year_published = book_data.get("publish_date", "0")
        
        if len(year_published) == 4:
            ind_book_dict["year_published"] = year_published
        elif len(year_published) == 0:
            ind_book_dict["year_published"] = "0"
        else:
            ind_book_dict["year_published"] = year_published[-4:]


        # Get Cover URL Path: 
        if "covers" in book_data:
            cover_id = book_data["covers"][0]
            cover_path = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
            ind_book_dict["Cover Path"] = cover_path
        else:
            ind_book_dict["Cover Path"] = "/static/images/blank_cover_img.png"
        

        # Get the ISBN_13 number if available: 
        isbn_request = requests.get(f"https://openlibrary.org/works/{book_OLID}/editions.json")
        isbn_data = isbn_request.json()

        if "entries" in isbn_data:
            entries_dict = isbn_data["entries"][0]
            isbn_13 = entries_dict.get("isbn_13", "0")
            ind_book_dict["isbn_13"] = isbn_13[0]
        else: 
            ind_book_dict["isbn_13"] = "0"
        

        # Get author_name 
        author_path_list = []
        if "authors" in book_data:
            authors_to_parse = book_data["authors"]
            # Getting list containing author's paths: 
            # if there is more than one author...
            if len(authors_to_parse) > 1:
                for item in authors_to_parse:
                    if "author" in item:
                        author_path_list.append(item["author"]["key"])
                    if "key" in item:
                        author_path_list.append(item["key"])
            # if there is one author...
            if len(authors_to_parse) == 1:
                if "key" in authors_to_parse[0]:
                    author_path_list.append(authors_to_parse[0]["key"])
                if "author" in authors_to_parse[0]:
                    author_path_list.append(authors_to_parse[0]["author"]["key"])

        # An empty list to append author names to. 
        author_names_list = []

        # If the list of author path routes is greater than or equal to one... 
        if len(author_path_list) >= 1: 
            for path in author_path_list:
                author_request = requests.get(f"https://openlibrary.org{path}.json")
                author_dict = author_request.json()

                if "name" in author_dict:
                    author_names_list.append(author_dict["name"])

                elif "personal_name" in author_dict:
                    author_names_list.append(author_dict["personal_name"])

            ind_book_dict["author_name"] = author_names_list
        # If no author's were found, set the key "author_name" to an empty list:
        else:
            ind_book_dict["author_name"] = author_names_list

        # Get Overview: 
        if "description" in book_data:
            if "value" in book_data["description"]:
                overview = book_data["description"]["value"]
            else:
                overview = book_data["description"]
        else:
            overview = "No overview for this book"

        ind_book_dict["overview"] = overview

        # Make a placeholder for an empty string for gender_identity 
        ind_book_dict["gender_identity"] = ""

        # Make a placeholder for an empty string for racial_identity 
        ind_book_dict["racial_identity"] = ""


        books_database[book_OLID]= ind_book_dict 

    out_file = open("books_database.json", "w")
    json.dump(books_database, out_file, indent = 4)
    out_file.close()

    return books_database 

################################################################################
# The function below needs commented out, or it'll make a new .json file every time! 
# create_database(book_OLIDs_list)
################################################################################





# Look back at notes on .get and values and methods and functions for dictionaries. 

# open and read the book_database.json (may have to stringify?)

# looping through and getting all of the values for each key 
    # then assign those values to a variable, and once I have the variables and
    # use these in the crud function to make an instance of a book, then add it 
    # to the session, and then commit. 

# define a function that opens and loads the data from the JSON file 


# Load book data from JSON file:
with open('static/books_database.json') as file:
    book_data = json.loads(file.read())


def seed_books():
    """This function loops through books_database.json and creates an 
    instantiation of a book object that matches the required fields of the 
    columns in the model.py tables."""
    
    # book_data.keys() --> this gives all of the individual dicts. within the db
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
    for key in book_data.keys():
        book_id = key
        gender_identity = book_data[key]["gender_identity"]
        racial_identity = book_data[key]["racial_identity"]
        # For future versions, I could change the database to include a list of 
        # characters to then iterate through like in seed_authors. 

        character_to_add = crud.add_character(book_id, gender_identity, 
                                              racial_identity)
        model.db.session.add(character_to_add)

        
def seed_authors():
    for key in book_data.keys():
        book_id = key
        # author name will be a list of author name/names. Is this okay?
        author_name = book_data[key]["author_name"]
        for author in author_name:
            author_to_add = crud.add_author(book_id, author)
            model.db.session.add(author_to_add)
    


# To test that functions are working correctly, execute the following command 
# in the command line: pg_dump books_db > books_practice.sql

def seed_database():
    """Run all seed functions to seed database """
    seed_books()
    seed_characters()
    seed_authors()
    model.db.session.commit() 
    print("All seed functions ran.")

seed_database()







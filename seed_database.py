"""Script to seed database"""

import requests 
import pprint 

books_database = {}

book_OLIDs_list = ["OL20914137W", "OL25074818W", "OL22020948W", "OL27139917W",
                   "OL26585018W", "OL21183636W", "OL19635091W", "OL20639677W", 
                   "OL27137338W", "OL20531661W", "OL25070735W", "OL39666203M", 
                   "OL24141019W", "OL20660371W", "OL46525616M", "OL24348919W", 
                   "OL46525603M", "OL19406W", "OL19987787W", "OL26886570M", 
                   "OL20055629W", "OL20128080W", "OL20128080W", "OL34975354M", 
                   "OL29531064M", "OL19743931W", "OL46525609M", "OL25873929W", 
                   "OL24327244W", "OL46525611M", "OL46525610M", "OL21874814W", 
                   "OL28716700M", "OL35289538M", "OL19667684W", "OL17072538M", 
                   "OL26977532M"]


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

    # Get author_img_path 

    # Make a placeholder for string gender_identity 


    # Get Overview: 
    if "description" in book_data:
        if "value" in book_data["description"]:
            overview = book_data["description"]["value"]
        else:
            overview = book_data["description"]
    else:
        overview = "No overview for this book"

    ind_book_dict["Overview"] = overview


    books_database[book_OLID]= ind_book_dict 

pprint.pprint(books_database)






# DICTIONARY-- make the key the book_ID and the value would be another dictionary
# as the values 


# Once I have ALL info, loop through the dictionary that I created and create an
# instantation object (a book) that would match the required fields of the columns
# in my model.py tables. 



# Notes for later when I need to add in character race and gender -- could make 
# a JSON obejct --> compiled_book_info.json --> can make an empty list the value of race and gender when intitailly making dict. 
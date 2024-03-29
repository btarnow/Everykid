"""These functions pull book information from OpenLibrary's Books and Authors 
APIs-- https://openlibrary.org/developers/api -- to generate my database"""

import requests 
import json

# These are the books included in my database: 
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
                   "OL20984012W", "OL20568318W", "OL27911917M", "OL12312396M",
                   "OL26265041W", "OL46060039M", "OL20198598W", "OL15980266W",
                   "OL26972693M"]


def get_title(book_data): 
    """Returns the title of a book"""
    
    title = book_data.get("title", "No title found")
    
    return title


def get_publish_date(book_data): 
    """Returns the publish date of a book if available. Otherwise returns 0"""
    
    year_published = book_data.get("publish_date", "0")

    if len(year_published) > 4: 
        year_published = year_published[-4:]
    
    return year_published


def get_cover_url_path(book_data):
    """Returns the url path for the image of a book's cover"""

    if "covers" in book_data:
        cover_id = book_data["covers"][0]
        cover_path = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
    else:
        cover_path = "/static/images/blank_cover_img.png"

    return cover_path


def get_isbn(book_OLID, book_data): 
    """Returns the ISBN number of a book if available. Otherwise it will 
    return '0' """

    if "isbn_13" in book_data: 
        isbn = book_data["isbn_13"][0]
    
    else: 
        isbn_request = requests.get(f"https://openlibrary.org/works/{book_OLID}/editions.json")
        isbn_data = isbn_request.json()

        if "entries" in isbn_data:
            entries_dict = isbn_data["entries"][0]
            isbn_13 = entries_dict.get("isbn_13", "0")
            isbn = isbn_13[0]
        else: 
            isbn = "0"
    
    return isbn


def get_authors_names(book_data):
    """Returns the name(s) of the author(s) of a book in the form of a list"""

    author_path_list = []
    author_names_list = []

    if "authors" in book_data:
        authors_to_parse = book_data["authors"]
        if len(authors_to_parse) > 1:
            for item in authors_to_parse:
                if "author" in item:
                    author_path_list.append(item["author"]["key"])
                if "key" in item:
                    author_path_list.append(item["key"])
        if len(authors_to_parse) == 1:
            if "key" in authors_to_parse[0]:
                author_path_list.append(authors_to_parse[0]["key"])
            if "author" in authors_to_parse[0]:
                author_path_list.append(authors_to_parse[0]["author"]["key"])

        if len(author_path_list) >= 1: 
            for path in author_path_list:
                author_request = requests.get(f"https://openlibrary.org{path}.json")
                author_dict = author_request.json()

                if "name" in author_dict:
                    author_names_list.append(author_dict["name"])

                elif "personal_name" in author_dict:
                    author_names_list.append(author_dict["personal_name"])
        
        elif "publishers" in book_data:
            author_names_list = book_data["publishers"]

    return author_names_list


def get_overview(book_data):
    """Returns the overview of a book if available. Otherwise, returns 
    'No overview for this book.' """

    if "description" in book_data:
        if "value" in book_data["description"]:
            overview = book_data["description"]["value"]
        else:
            overview = book_data["description"]
    else:
        overview = "No overview for this book"

    return overview


def create_database(book_OLIDs_list):
    """This function pulls data from the Open Library API to generate the database"""

    books_database = {}

    for book_OLID in book_OLIDs_list:
        ind_book_dict = {}
        book_request = requests.get(f"https://openlibrary.org/works/{book_OLID}.json")
        book_data = book_request.json()
        print(book_data)

        ind_book_dict["title"] = get_title(book_data)
        ind_book_dict["year_published"] = get_publish_date(book_data)
        ind_book_dict["Cover Path"] = get_cover_url_path(book_data)
        ind_book_dict["isbn_13"] = get_isbn(book_OLID, book_data)
        ind_book_dict["author_name"] = get_authors_names(book_data)
        ind_book_dict["overview"] = get_overview(book_data)

        # Gender and racial identity placeholder strings: 
        ind_book_dict["gender_identity"] = ""
        ind_book_dict["racial_identity"] = ""

        books_database[book_OLID]= ind_book_dict 

    out_file = open("books_database.json", "w")
    json.dump(books_database, out_file, indent = 4)
    out_file.close()

    return books_database 

create_database(book_OLIDs_list)

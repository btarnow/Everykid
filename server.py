"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud
import model
import random 

app = Flask(__name__)


@app.route('/')
def homepage():
    """Return homepage"""   

    return render_template("homepage.html")


@app.route('/book_filters')
def apply_book_filters():
    """Return filtered results page"""   

    race_filter = request.args.get("race")
    gender_filter = request.args.get("gender")

    if not race_filter:
        race_filter = "ALL RACES"
    
    if not gender_filter:
        gender_filter = "ALL GENDERS"

    
    characters = crud.filter_characters(race_filter, gender_filter)

    book_list = []
    for character in characters:
        book_list.append(character.book)
    
    return render_template("book_results_page.html", book_list=book_list, 
                           race_filter=race_filter, gender_filter=gender_filter)


@app.route('/book_results_page/<book_id>')
def show_book_details(book_id):
    """Displays detailed book information"""

    book = crud.get_book_by_id(book_id)
    char_race = book.characters[0].racial_identity 
    char_gender = book.characters[0].gender_identity
    
    similar_race_characters = crud.find_similar_race_characters(char_race)
    similar_gender_characters = crud.find_similar_gender_characters(char_gender)

    recommended_books = []
    for character in similar_race_characters:
        recommended_books.append(character.book)
    for character in similar_gender_characters:
        recommended_books.append(character.book)
    recommended_books.remove(book)

    four_recs = set(random.sample(recommended_books, 4))

    return render_template("book_details.html", book=book, four_recs=four_recs) 



if __name__ == "__main__":
    model.connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)
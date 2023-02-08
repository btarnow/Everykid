"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud
import model

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

    #TODO: 
    ######## FIX THIS CODE TOMORROW: ###################
    # char_race = book.racial_identity 
    # char_gender = book.gender_identity 

    # similar_race_characters = crud.find_similar_characters(char_race)

    # recommended_books_race = []
    # for character in similar_race_characters:
    #     recommended_books_race.append(character.book)
    #############################################################

    return render_template("book_details.html", book=book) 



if __name__ == "__main__":
    model.connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)
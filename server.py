"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud
import model

app = Flask(__name__)


@app.route('/')
def homepage():
    """Return homepage"""   

    return render_template("homepage.html")


#/book_filters is the action of the form on the homepage
@app.route('/book_filters')
def apply_book_filters():
    """Return filtered results page"""   

    # when using request.args.get with a select tag in HTML, the name of the 
    # select tag will be the key, and the value will be whatever the option 
    # value attribute is that is selected by the user (i.e. <option value="Asian">
    race_filter = request.args.get("race")
    gender_filter = request.args.get("gender")

    # to account for if the user does not select one or both filters, this will 
    # still allow for books to show up since it's passing a value through to 
    # make a query string. 
    if not race_filter:
        race_filter = "ALL RACES"
    
    if not gender_filter:
        gender_filter = "ALL GENDERS"

    # get all of the characters that match the specified filters
    characters = crud.filter_characters(race_filter, gender_filter)

    # get the books associated with each character and append them to a list
    book_list = []
    for character in characters:
        book_list.append(character.book)

    # the list of books then gets passed to the books_results_page where it can
    # be iterated through using a Jinja loop. 
    
    return render_template("book_results_page.html", book_list = book_list, 
                           race_filter = race_filter, gender_filter = gender_filter)


@app.route('/book_results_page/<book_id>')
def show_book_details(book_id):
    """Displays detailed book information"""

    book = crud.get_book_by_id(book_id)

    return render_template("book_details.html", book = book)   





if __name__ == "__main__":
    model.connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)
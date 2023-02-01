"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud
import model

app = Flask(__name__)


# Replace this with routes and view functions!
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

   
    # once I have all of the characters, get the book associated with each one 
    # and put them into a list. This list of books would then go into my template. 

    # this will be a list of character objects
    characters = crud.filter_characters(race_filter, gender_filter)

    # get the book associated with each character and append that to a list
    book_list = []
    for character in characters:
        book_list.append(character.book)

    # the list of books then gets passed to the books_results_page where it can
    # be iterated through using a Jinja loop. 
    return render_template("book_results_page.html", book_list = book_list)




if __name__ == "__main__":
    model.connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)
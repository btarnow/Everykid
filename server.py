"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud

app = Flask(__name__)


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """Return homepage"""   

    return render_template("homepage.html")

@app.route('/book_filters')
def apply_book_filters():
    """Return filtered results page"""   

    # when using request.args.get with a select tag in HTML, the name of the 
    # select tag will be the key, and the value will be whatever the option 
    # value attribute is that is selected by the user (i.e. <option value="Asian">
    race_filter = request.args.get("race")
    gender_filter = request.args.get("gender")

    # once crud function is created, call the function here. --> pass in race_filter and gender_filter
    # once I have all of the characters, get the book associated with each one 
    # and put them into a list. This list of books would then go into my template. 
    crud.filter_characters(race_filter, gender_filter)

    return render_template("book_results_page.html")




if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
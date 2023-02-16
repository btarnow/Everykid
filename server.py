"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud
import model
import random 
from passlib.hash import argon2

app = Flask(__name__)
app.secret_key = 'RANDOM SECRET KEY'

@app.route('/')
def homepage():
    """Return homepage"""
  
    return render_template("homepage.html")


# # TODO: Most likely delete (this maps to the login button I had in the nav bar)
# @app.route('/route_to_login')
# def show_login_page():
#     """Return login page"""
    
#     return render_template("login_page.html")


@app.route('/route_to_user_page')
def show_user_page():
    """Return user_page page"""

    user_id = session.get('user_id')
    
    if user_id:
        return redirect (f"/user_page/{user_id}")

    else: 
        return render_template("login_page.html")


@app.route('/user_page/<user_id>')
def user_page(user_id):
    """Display user's homepage"""
    
    user = crud.get_user_by_id(user_id)

    my_books_collection = crud.create_collection(user_id, "My Books")

    #TODO: do a get request to get the name of the collection and then use the 
    # create_collection crud function OR could I do this with AJAX? Would need 
    # some help getting started...

    

    return render_template('user_page.html', user=user, my_books_collection=my_books_collection)


@app.route('/login', methods=["POST"])
def login():
    """Process user login"""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    
    if user is None:
        flash("User does not exist. Please try again!")
        return render_template("login_page.html")
    
    if argon2.verify(password, user.password):
        session['user_id'] = user.user_id 
        return redirect ("/")
    else:
        flash("Passwords do not match. Please try again.")
        return render_template("login_page.html")


@app.route('/signup', methods=["POST"])
def signup():
    """Create a new user"""
    email = request.form.get("email")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    password = request.form.get("password")

    hashed_password = argon2.hash(password)
    del password

    existing_user = crud.get_user_by_email(email)

    if existing_user:
        flash("User already exists.")
        return render_template("login_page.html")

    else:
        user = crud.create_user(email=email, password=hashed_password, 
                                    fname=fname, lname=lname)
        model.db.session.add(user)
        model.db.session.commit()
        session["user_id"] = user.user_id
        
        my_books_collection = crud.create_collection(user.user_id, "My Books")
        model.db.session.add(my_books_collection)
        model.db.session.commit()

        flash("Account created!")
        return redirect ("/")


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
    book_set = set(book_list)
    book_list = list(book_set)
    
    #if the user is signed in, return this PLUS the user's information
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

    #TODO: a button that's a bookmark for each book and when clicked it would 
    # send to a get request to get the book_id, store it in a session, plug it 
    # into the crud function book_to_add, then add that to the database

    return render_template("book_details.html", book=book, four_recs=four_recs) 


if __name__ == "__main__":
    model.connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)
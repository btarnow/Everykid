"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect
import crud
import model 
import random 
from passlib.hash import argon2


app = Flask(__name__)
app.secret_key = 'RANDOM SECRET KEY'


# ----- ROUTES FOR HOMEPAGE/LOGIN ----- #
@app.route('/')
def homepage():
    """Return homepage"""
  
    return render_template("homepage.html")


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

        return redirect ("/")
    

@app.route('/logout')
def logout():
    """Log user out"""

    session.pop('user_id', None)

    return redirect('/')


# ----- ROUTES FOR USER PAGE ----- #
@app.route('/route_to_user_page')
def show_user_page():
    """Return user_page page if logged in, or returns log in page"""

    user_id = session.get('user_id')
    
    if user_id:
        return redirect (f"/user_page/{user_id}")

    else: 
        return render_template("login_page.html")
    

@app.route('/user_page/<user_id>')
def user_page(user_id):
    """Display user's homepage"""

    user = crud.get_user_by_id(user_id)
    collection = crud.get_users_mybooks_collection(user_id)

    return render_template('user_page.html', user=user, collection=collection)


# ----- ROUTES FOR BOOK RESULTS AND DETAILS PAGES ----- #
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
    
    return render_template("book_results_page.html", book_list=book_list, 
                           race_filter=race_filter, gender_filter=gender_filter)


@app.route('/book_results_page/<book_id>')
def show_book_details(book_id):
    """Displays detailed book information"""

    user_id = session.get('user_id')
    book = crud.get_book_by_id(book_id)

    if user_id is None:
        check_if_in_collection = None
    else: 
        collection = crud.get_users_mybooks_collection(user_id)
        check_if_in_collection = crud.check_if_book_in_collection(book_id, 
                                                            collection.collection_id)

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

    five_recs = set(random.sample(recommended_books, 5))

    return render_template("book_details.html", book=book, five_recs=five_recs, 
                           check_if_in_collection=check_if_in_collection) 


@app.route('/add_book')
def add_book():
    """Add book to collection"""

    user_id = session.get('user_id')
    book_id = request.args.get('book_id')
    collection = crud.get_users_mybooks_collection(user_id)

    check_if_in_collection = crud.check_if_book_in_collection(book_id, 
                                                    collection.collection_id)
    
    if check_if_in_collection is None:
        book_to_add = crud.add_book_to_collection(book_id, collection.collection_id)
    
        model.db.session.add(book_to_add)
        model.db.session.commit()
        
        return collection.collection_name
    
    else:
        pass


@app.route('/remove_book_from_details')
def remove_book():
    """Remove book from collection from book details page"""

    user_id = session.get('user_id')
    book_id = request.args.get('book_id')
    
    collection = crud.get_users_mybooks_collection(user_id)
    book_to_delete = crud.delete_book_from_collection(book_id, 
                                                    collection.collection_id)
   
    model.db.session.delete(book_to_delete)
    model.db.session.commit()
    
    return collection.collection_name


# ----- ROUTES FOR BOOK ABOUT PAGES ----- #
@app.route('/story')
def show_story():
    """Displays the story page"""

    return render_template("story.html")


@app.route('/identities')
def show_identity_page():
    """Displays the story page"""

    return render_template("identities.html")



if __name__ == "__main__":
    model.connect_to_db(app, echo=False)
    app.run(host="0.0.0.0")
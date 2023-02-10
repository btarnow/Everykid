
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    """A book."""

    __tablename__ = "books"

    # Book_id is not set to auto-increment because it will automatically be a
    # unique ID from the OpenLibrary API. 
    book_id = db.Column(db.String, primary_key=True)
    isbn_13 = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    year_published = db.Column(db.String, nullable=False)
    cover_path = db.Column(db.String, nullable=False)
    overview = db.Column(db.Text, nullable=False)

    characters = db.relationship("Character", back_populates="book")
    collections = db.relationship("Collection", back_populates="book")
    ratings_and_reviews = db.relationship("Rating_and_Review", back_populates="book")
    authors = db.relationship("Author", back_populates="book")
    

    def __repr__(self):
        """Showing the title and book id of a Book object"""

        return f"<Title: {self.title}, Book ID: {self.book_id}>"


class Author(db.Model):
    """An author."""

    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.String, db.ForeignKey("books.book_id"))
    author_name = db.Column(db.String, nullable=False)
    # Can include the following if I have time to add author images
    # author_img_path = db.Column(db.String, nullable=True)


    book = db.relationship("Book", back_populates="authors")


    def __repr__(self):
        """Showing the author id and author name of an Author object"""

        return f"<Author ID: {self.author_id}, Name: {self.author_name}>"
    

class Character(db.Model):
    """A primary character in a book."""

    __tablename__ = "characters"

    character_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    racial_identity = db.Column(db.String, nullable=False)
    gender_identity = db.Column(db.String, nullable=False)
    book_id = db.Column(db.String, db.ForeignKey("books.book_id"))

    book = db.relationship("Book", back_populates="characters")
    

    def __repr__(self):
        """Showing the character ID of a Character object"""

        return f"<Character ID: {self.character_id}>"
    

class User(db.Model):
    """A User."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)

   
    collections = db.relationship("Collection", back_populates="user")
    ratings_and_reviews = db.relationship("Rating_and_Review", back_populates="user")
 

    def __repr__(self):
        """Showing the first and last name and username of a User object"""

        return f"<Name: {self.fname} {self.lname}, Username: {self.username}>"


class Rating_and_Review(db.Model):
    """A book rating of 1-5 stars and an optional review comment"""

    __tablename__ = "ratings_and_reviews"

    rating_review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    book_id = db.Column(db.String, db.ForeignKey("books.book_id"))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=True)

    
    user = db.relationship("User", back_populates="ratings_and_reviews")
    book = db.relationship("Book", back_populates="ratings_and_reviews")


    def __repr__(self):
        """Showing the rating/review id of an object."""

        return f"<Rating/Review ID: {self.rating_review_id}>"
    

class Collection(db.Model):
    """A user's collection of books"""

    __tablename__ = "collections"

    collection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    book_id = db.Column(db.String, db.ForeignKey("books.book_id"))
    collection_name = db.Column(db.String, nullable=False)
    
    user = db.relationship("User", back_populates="collections")
    book = db.relationship("Book", back_populates="collections")


    def __repr__(self):
        """Showing the collection name of a Collection object."""

        return f"<Collection Name: {self.collection_name}>"
    


def connect_to_db(flask_app, db_uri="postgresql:///books_db", echo=False):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    app.app_context().push()
    db.create_all()
    connect_to_db(app, echo=False) 
                        # ^ If echo=True, output will show in terminal
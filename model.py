"""Models for EveryKid app."""

# Flask SQLAlchemy is a object-relational-mapper that translates Python classes 
# to tables on relational databases and automatically converts function calls to 
# SQL statements
from flask_sqlalchemy import SQLAlchemy

# db is a SQLAlchemy object 
db = SQLAlchemy()

# Notes on classes below: 
    # Nullable = FALSE --> means the user HAS to give an input

    # DateTime documentation: https://strftime.org/
        # datetime.strptime(date_string, format)
        # >>> date_str = "31-Oct-2015"
        # >>> format = "%d-%b-%Y"
        # >>> date = datetime.strptime(date_str, format)
        # Need to include --> from datetime import datetime

    # The classes will inherit everything that exists in db.Model. db is the 
    # SQLAlchemy object that is the "magic" behind the scenes

class Book(db.Model):
    """A book."""

    __tablename__ = "books"

    # Possibly make this book_id & do autoincrement=True if ISBN doesn't work out
    book_ISBN = db.Column(db.Integer, primary_key=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    # Might change year_published to an int instead of DateTime... 
    year_published = db.Column(db.DateTime, nullable=False)
    cover_path = db.Column(db.String, nullable=False)
    overview = db.Column(db.String, nullable=False)
    # Nice to haves... 
    # author_img_path = db.Column(db.String, nullable=True)

    characters = db.relationship("Character", back_populates="book")
    

    def __repr__(self):
        """Showing the title and ISBN of an object"""

        return f"<Title: {self.title}, ISBN: {self.book_ISBN}>"
    

class Character(db.Model):
    """A primary character in a book."""

    __tablename__ = "characters"

    character_id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
                                                               nullable=False)
    racial_identity = db.Column(db.String, nullable=False)
    gender_identity = db.Column(db.String, nullable=False)
    book_ISBN = db.Column(db.Integer, db.ForeignKey("books.book_ISBN"), 
                                                        nullable=False)
    
    book = db.relationship("Book", back_populates="characters")


    def __repr__(self):
        """Showing the racial and gender identities of an object"""

        return f"<Race: {self.racial_identity}, Gender: {self.gender_identity}>"



#need to add correct db_name
def connect_to_db(flask_app, db_uri="postgresql:///{db_name}", echo=True):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == "__main__":
    from server import app

    connect_to_db(app, echo=False) # If echo=True, output will show in terminal
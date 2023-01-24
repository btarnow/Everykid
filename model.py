"""Models for EveryKid app."""

# Flask SQLAlchemy is a object-relational-mapper that translates Python classes 
# to tables on relational databases and automatically converts function calls to 
# SQL statements
from flask_sqlalchemy import SQLAlchemy

# db is a SQLAlchemy object 
db = SQLAlchemy()



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
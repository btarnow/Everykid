"""Server for EveryKid app."""

from flask import Flask, request, render_template, flash, session, redirect

app = Flask(__name__)


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """Return homepage"""   

    return render_template("homepage.html")


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
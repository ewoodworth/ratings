"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    # a = jsonify([1,3])
    #SETUP SESSION W?USER KEY NULL START< FILL UPON ESTABLISHMENT
    # current_user = session.get(current_user:{username:, }, 0)
    
    return render_template("homepage.html")

# @app.route('/dbcheck', methods=['POST'])
# def dbcheck():
#     """Check password against databse"""
#     potential_input = request.form.get("username")
#     potential = User.query.filter_by(username=potential_input).first()
#     if potential
#         return True  ##JSONIIFY RESULT FOR JS METABOLISM

@app.route('/signup_catch', methods=['POST'])
def signup_catch():
    """Collect results from signup form"""
    potential_input = request.form.get("username")
    potential = User.query.filter_by(username=potential_input).first()
    if potential:
        flash("Username already taken! Please try again!")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        age = request.form.get("age")
        zipcode = request.form.get("zipcode")
        user = User(user_id=user_id, username=username, password=password, age=age, zipcode=zipcode)
        db.session.add(user)
        db.session.commit()



    return redirect('/')


@app.route('/login_catch', methods=['POST'])
    # """Collect results from login form"""
    #check database for user id #On failure: FLASH 
    #Check matching password #On failure FLASH
    # return redirect('/')

@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5003)

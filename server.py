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
#Fix server-side caching issues
app.jinja_env.auto_reload = True

@app.route('/')
def index():
    """Homepage."""
    if 'current_user' in session:
        #How to render a page if they are already signed inde
        flash('You are signed up and logged in!')
        return render_template('homepage.html')
    else:
        # current_user = session['current_user'] = {} 
        #how to render a page for login/signin
        flash('You are logged out! Please log in below!')
        return render_template('signup.html')


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
        user = User(username=username, password=password, age=age, zipcode=zipcode)
        db.session.add(user)
        db.session.commit()
        #create session cookie for this browser session
        session['current_user'] = {'username':username}


    return redirect('/')


@app.route('/login_catch', methods=['POST'])
def login_catch():
    """Collect results from login form"""
    username = request.form.get("username")
    password = request.form.get("password")
    check_username = User.query.filter_by(username=username).first()
    check_password = User.query.filter_by(password=password).first()
    session['current_user'] = {'username':username}
    if check_username and check_password:
        return redirect('/')
    else:
        flash('Your username and password were not recognized')
        return redirect('/')

@app.route('/logout_catch', methods=['POST'])
def logout_catch():
    """Log user out, redirect home"""
    session.clear()
    return redirect('/')

@app.route("/users")
def user_list():
    """Show list of users."""
    users = User.query.all()
    return render_template("user_list.html", users=users, user_id=users.user_id)

@app.route("/users/{{ user_id }}")
def user_page(user_id):
    """Show user page """
    user = User.query.filter_by(username=username)
    age = user.age
    zipcode = user.zipcode
    ratings=
#User age
#user ZIP
#LIST OF RATED MOVIES (from that user)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5003)

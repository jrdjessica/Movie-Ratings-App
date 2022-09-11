"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.return_movies()

    return render_template("all_movies.html", movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route('/users')
def all_user():
    """Display the email addresses of each user and link to user profile."""

    users = crud.return_user()

    return render_template("all_users.html", users=users)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show info from a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Creates a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash('That email is being used already. Try another email.')
    else:
        user = crud.create_user(email, password)
        flash('Your account was successfully created. Please log in.')
        db.session.add(user)
        db.session.commit()

    return redirect('/')


@app.route('/login', methods=['POST'])
def log_in():
    """Log in."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user and user.password == password:
        session['user_email'] = user.email
        flash('Logged in successfully.')
    else:
        flash('Log in unsuccessful. Try again.')

    return redirect('/')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

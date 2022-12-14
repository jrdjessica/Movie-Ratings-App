"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def return_user():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return user from user ID."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Returns user with email if it exists."""

    return User.query.filter(User.email == email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview,
                  release_date=release_date, poster_path=poster_path)

    return movie


def return_movies():
    """Return all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Return movie from movie ID."""

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating


def update_rating(rating_id, score):
    """Update movie rating."""

    rating = Rating.query.get(rating_id)
    rating.score = new_score


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

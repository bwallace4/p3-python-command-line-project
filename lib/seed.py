from faker import Faker
import random
from sqlalchemy.orm.exc import NoResultFound
from models import Director, Movie, Review, Session

fake = Faker()

session = Session()

def add_movie(title, length, director_id):
    try:
        existing_movie = session.query(Movie).filter_by(title=title).one()
        print("Movie already exists.")
    except NoResultFound:
        new_movie = Movie(title=title, movie_length=length, director_id=director_id)
        session.add(new_movie)
        session.commit()
        print("Movie added successfully.")

def add_director(name, number_of_films, nationality, birthday):
    new_director = Director(name=name, number_of_films=number_of_films, nationality=nationality, birthday=birthday)
    session.add(new_director)
    session.commit()
    print("Director added successfully.")

def add_review(movie_id, rating, comment):
    new_review = Review(movie_id=movie_id, rating=rating, comment=comment)
    session.add(new_review)
    session.commit()
    print("Review added successfully.")

def add_random_data():
    for _ in range(10):
        director_name = fake.name()
        number_of_films = random.randint(1, 50)
        nationality = fake.country()
        birthday = fake.date_of_birth(minimum_age=25, maximum_age=80) 

        add_director(director_name, number_of_films, nationality, birthday)

    directors = session.query(Director).all()
    for _ in range(20):
        title = fake.catch_phrase()
        length = random.randint(60, 180)
        director = random.choice(directors)

        add_movie(title, length, director.id)

    movies = session.query(Movie).all()
    for _ in range(30):
        movie = random.choice(movies)
        rating = random.randint(1, 10)
        comment = fake.paragraph()

        add_review(movie.id, rating, comment)

if __name__ == "__main__":
    add_random_data()

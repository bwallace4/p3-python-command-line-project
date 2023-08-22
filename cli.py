from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Director, Movie, Review,engine

Session = sessionmaker(bind=engine)
session = Session()

def create_director(name,number_of_films,nationality):
    director = Director(name=name,number_of_films=number_of_films,nationality=nationality)
    session.add(director)
    session.commit()

def create_movie(title, director_id,movie_length):
    movie = Movie(title=title,movie_length=movie_length, director_id=director_id)
    session.add(movie)
    session.commit()

def create_review(movie_id, rating, comment):
    review = Review(movie_id=movie_id, rating=rating, comment=comment)
    session.add(review)
    session.commit()

def read_movies():
    movies = session.query(Movie).all()
    for movie in movies:
        director_name = movie.director.name if movie.director else "Indy Film"
        print(f"ID: {movie.id}, Title: {movie.title}, Director: {director_name}")



def main():
    while True:
        print("1. Add Movie")
        print("2. List Movies")
        print("3. Add Review")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter movie title: ")
            director_id = int(input("Enter director ID: "))
            create_movie(title, director_id)
        elif choice == '2':
            read_movies()
        elif choice == '3':
            movie_id = int(input("Enter movie ID: "))
            rating = int(input("Enter rating: "))
            comment = input("Enter comment: ")
            create_review(movie_id, rating, comment)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()

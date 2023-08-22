# from models import Director, Movie, Review, Session

# def main():
#     session = Session()

#     # Create directors
#     director1 = Director(name="Director 1",nationality= "england")
#     director2 = Director(name="Director 2")

#     # Create movies with associated directors
#     movie1 = Movie(title="Movie 1", director=director1)
#     movie2 = Movie(title="Movie 2", director=director2)

#     # Create reviews for movies
#     review1 = Review(rating=5, comment="Great movie!", movie=movie1)
#     review2 = Review(rating=4, comment="Enjoyed it.", movie=movie2)

#     # Add data to session and commit
#     session.add_all([director1, director2, movie1, movie2, review1, review2])
#     session.commit()

#     # Query example: Get all movies and their directors
#     movies_with_directors = session.query(Movie).all()
#     for movie in movies_with_directors:
#         print(f"Movie: {movie.title}, Director: {movie.director.name}")





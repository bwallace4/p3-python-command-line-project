
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

 
Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_of_films = Column(Integer)
    birthday = Column(DateTime())
    nationality = Column(String,nullable=True)
    movies = relationship("Movie", backref="director")


    def __init__(self,name, birthday, number_of_films, nationality):
        self.name = name
        self.birthday= birthday
        self.number_of_films = number_of_films
        self.nationality = nationality

    def __repr__(self):
        return f"Director(id='{self.id}', name={self.name}, birthday={self.birthday} number_of_films={self.number_of_films}, nationality={self.nationality})"
 

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer,  primary_key=True)
    title = Column(String)
    movie_length = Column(Integer) 
    director_id = Column(Integer, ForeignKey('directors.id')) 
    reviews = relationship("Review", backref="movie",)

    def __init__(self, title ,movie_length, director_id):
        self.title = title
        self.movie_length = movie_length
        self.director_id = director_id

     

    def __repr__(self):
        return f"Movie(id='{self.id}', title={self.title}, movie_length= {self.movie_length}, director_id={self.director_id})"
 


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    movie_id = Column(Integer, ForeignKey('movies.id'),nullable=True)

    def __init__(self, rating, comment, movie_id ):
        self.rating = rating
        self.comment = comment
        movie_id = movie_id
    
        


    def __repr__(self):
        return f"Review(id='{self.id}', rating={self.rating}, comment={self.comment}, movie_id={self.movie_id})"
 


engine = create_engine('sqlite:///library.db', echo=True)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
directors_data = [
    ("Martin Scorsese", 50, "American", datetime(year=1942, month=11, day=17)),
    ("Christopher Nolan", 10, "British", datetime(year=1970, month=7, day=30))
]

for name, number_of_films, nationality, birthday in directors_data:
    director = Director(name=name, number_of_films=number_of_films, nationality=nationality, birthday=birthday)
    session.add(director)


movies_data = [
    {"title": "The Godfather", "movie_length": 175, "director_id": 1},
    {"title": "Inception", "movie_length": 148, "director_id": 2}
]

for movie_data in movies_data:
    movie = Movie(**movie_data)
    session.add(movie)


for rating in range(1, 1):
    review = Review(rating=rating, comment=f"Review for rating {rating}", movie_id=1)
    session.add(review)


review_data = {
    "rating": 9,
    "comment": "A classic film by Martin Scorsese.",
    "movie_id": 3
}

review = Review(**review_data)
session.add(review)
session.commit()

director = Director( name= "Spike Lee", number_of_films=52, nationality="American", birthday=
datetime(
year = 1957, month= 3, day = 20))
session.add(director)
session.commit()

movie = Movie( "Do the right thing", 120, 2)
session.add(movie)
session.commit()

review = Review( 7 ,"Do The Right Thing is a great joint by Spike Lee. Do The Right Thing explains summer in New York really well. It's a very good film to watch", 1)
session.add (review)
session.commit()
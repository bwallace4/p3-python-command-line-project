from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, )
    name = Column(String)
    number_of_films = Column(Integer)
    nationality = Column(String)
    movies = relationship("Movie", backref="director", lazy=True)


    def __init__(self, id,name, number_of_films, nationality):
        self.id = id
        self.name = name
        self.number_of_films = number_of_films
        self.nationality = nationality

    def __repr__(self):
        return f"Director(id='{self.id}', name={self.name}, number_of_films={self.number_of_films}, nationality={self.nationality})"
 

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer,  primary_key=True)
    title = Column(String)
    movie_length = Column(Integer) 
    director_id = Column(Integer, ForeignKey('directors.id'))
    reviews = relationship("Review", backref="movie", lazy=True)

    def __init__(self, id,title,movie_length,director_id):
        self.id = id
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
    movie_id = Column(Integer, ForeignKey('movies.id'))

    def __init__(self, id, rating, comment, movie_id):
        self.id = id
        self.rating = rating
        self.comment = comment
        movie_id = movie_id


    def __repr__(self):
        return f"Review(id='{self.id}', rating={self.rating}, comment={self.comment}, movie_id={self.movie_id})"
 

# Create an engine and session
engine = create_engine('sqlite:///movies.db', echo=True)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

director = Director( 1 ,"Spike Lee", 52, "American")
session.add(director)
session.commit()

movie = Movie( 2, "Friday", 91, 1)
session.add(movie)
session.commit()

review = Review(1, 7 ,"This film is a laugh a minute and portrays realistic characters each of us can relate to", 2)
session.add (review)
session.commit()
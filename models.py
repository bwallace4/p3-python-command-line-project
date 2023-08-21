# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    movies = relationship("Movie", backref="director", lazy=True)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))
    reviews = relationship("Review", backref="movie", lazy=True)

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    movie_id = Column(Integer, ForeignKey('movies.id'))

# Create an engine and session
engine = create_engine('sqlite:///movies.db', echo=True)
Session = sessionmaker(bind=engine)


# def __repr__(self):
#         return f"User {self.id}: "\
#              + f"{self.username} "\
#              + f"email: {self.email}\n"




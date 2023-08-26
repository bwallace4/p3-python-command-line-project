#!/usr/bin/env python3
from datetime import datetime
import click
from sqlalchemy.orm import sessionmaker
from models import Base, Director, Movie, Review, engine

Session = sessionmaker(bind=engine)
session = Session()

@click.command()
def create_director():
    name = click.prompt("Enter director name")
    birthday_str = click.prompt("Enter director's birthday (YYYY-MM-DD)")

    try:
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    except ValueError:
        click.echo("Invalid date format. Please use YYYY-MM-DD.")
        return
    number_of_films = click.prompt("Enter number of films directed", type=int)
    nationality = click.prompt("Enter nationality")
    director = Director(name=name,birthday=birthday, number_of_films=number_of_films, nationality=nationality)
    session.add(director)
    session.commit()
    click.echo("Director created!")

@click.command()
def create_movie():
    title = click.prompt("Enter movie title")
    director_id = click.prompt("Enter director ID", type=int)
    movie_length = click.prompt("Enter movie length", type=int)
    movie = Movie(title=title, director_id=director_id, movie_length=movie_length)
    session.add(movie)
    session.commit()
    click.echo("Movie created!")

@click.command()
def create_review():
    movie_id = click.prompt("Enter movie ID", type=int)
    rating = click.prompt("Enter rating", type=int)
    comment = click.prompt("Enter comment")
    review = Review(movie_id=movie_id, rating=rating, comment=comment)
    session.add(review)
    session.commit()
    click.echo("Review created!")

@click.command()
def list_movies():
    movies = session.query(Movie).all()
    for movie in movies:
        director_name = movie.director.name if movie.director else "Unknown Director"
        click.echo(f"ID: {movie.id}, Title: {movie.title}, Director: {director_name}")

@click.group()
def cli():
    pass

cli.add_command(create_director)
cli.add_command(create_movie)
cli.add_command(create_review)
cli.add_command(list_movies)

if __name__ == "__main__":
    cli()

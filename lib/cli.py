import click
from sqlalchemy.orm import sessionmaker
from models import Director, Movie, engine

Session = sessionmaker(bind=engine)
session = Session()

@click.command()
def main():
    click.echo(" Welcome to DirectMe: Your Movie Director Database")
    while True:
        user_input = click.prompt("Enter a command (type 'help' for options, or 'exit' to quit):", type=str)
        if user_input.lower() == 'exit':
            break
        elif user_input == 'greet':
            name = click.prompt("Enter your name:", type=str)
            click.echo(f"Hello, {name}!")
        elif user_input.lower() == 'help':
            display_help()
        elif user_input.lower() == 'create_director':
            create_director()
        elif user_input.lower() == 'add_movie':
            add_movie()
        elif user_input.lower() == 'list_directors':
            list_directors()
        elif user_input.lower() == 'list_movies':
            list_movies()
        else:
            click.echo("Unknown command. Type 'help' for available options.")

def display_help():
    click.echo("Available Commands:")
    click.echo("1. greet - Greet the user")
    click.echo("2. create_director - Create a director")
    click.echo("3. add_movie - Add a new movie")
    click.echo("4. list_directors - List all directors")
    click.echo("5. list_movies - List all movies")
    click.echo("6. exit - Quit the program")

def add_movie():
    click.echo("Adding a New Movie")
    title = click.prompt("Enter the movie title:", type=str)
    movie_length = click.prompt("Enter the movie length (in minutes):", type=int)
    director_id = click.prompt("Enter the director's ID:", type=int)

    new_movie = Movie(title=title, movie_length=movie_length, director_id=director_id)
    session.add(new_movie)
    session.commit()
    click.echo("Movie added successfully.")

def create_director():
    click.echo("Creating a new director:")
    name = click.prompt("Enter director's name:", type=str)
    number_of_films = click.prompt("Enter the number of films directed:", type=int)
    nationality = click.prompt("Enter director's nationality:", type=str)
    birthday = click.prompt("Enter director's birthday (YYYY-MM-DD):", type=str)

    try:
        birthday = click.DateTime()(birthday)
    except ValueError:
        click.echo("Invalid date format. Please use YYYY-MM-DD.")
        return

    director = Director(name=name, number_of_films=number_of_films, nationality=nationality, birthday=birthday)
    session.add(director)
    session.commit()
    
    click.echo("Director created successfully!")

def list_directors():
    click.echo("List of Directors:")
    directors = session.query(Director).all()
    for director in directors:
        click.echo(f"Director ID: {director.id}, Name: {director.name}")

def list_movies():
    click.echo("List of Movies:")
    movies = session.query(Movie).all()
    for movie in movies:
        click.echo(f"Movie Title: {movie.title}, Length: {movie.movie_length} minutes, Director ID: {movie.director_id}")

if __name__ == '__main__':
    main()




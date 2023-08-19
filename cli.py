import sqlite3

conn = sqlite3.connect('models.db')
cursor = conn.cursor()
import click

@click.command()
@click.argument('username')
@click.argument('email')
def add_record(username, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (username, email))
    conn.commit()
    click.echo("Record added successfully!")

@click.command()
@click.argument('user_id')
@click.argument('new_email')
def update_email(user_id, new_email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    conn.commit()
    click.echo("Email updated successfully!")

# More command handlers...

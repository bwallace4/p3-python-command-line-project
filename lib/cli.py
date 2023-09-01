import click

@click.command()
def main():
    click.echo("Welcome to My CLI App!")
    while True:
        user_input = click.prompt("Enter a command (or 'exit' to quit):", type=str)
        if user_input.lower() == 'exit':
            break
        elif user_input == 'greet':
            name = click.prompt("Enter your name:", type=str)
            click.echo(f"Hello, {name}!")
        else:
            click.echo("Unknown command. Try again.")

if __name__ == '__main__':
    main()


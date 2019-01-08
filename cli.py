import click

# function that runs from CLI:
# Command 1: --run [] [] [] : does the damn thing.


@click.command()
def cli():
    click.echo("Hello World")


# Who knows why I wrote this
with open('.gitignore.txt') as giti:
    click.echo(giti.read().split('\n'))


# Function that configures a configuration.yaml
@click.command()
def configure():
    user = click.prompt('What is your username?')
    click.echo("Remember to set your password! We might encrypt with click later.")
    path = click.prompt('What is the filepath?')
    dict = {'auth_userId': user, 'auth_passwd': '', 'filepath': path}

    pass


if __name__ == "__main__":
    cli()

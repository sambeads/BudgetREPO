import click

# function that runs from CLI:
# Command 1: --run [] [] [] : does the damn thing.


@click.command()
def cli():
    click.echo("Hello World")

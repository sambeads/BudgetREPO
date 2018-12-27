import click

# function that runs from CLI:
# Command 1: --run [] [] [] : does the damn thing.

@click.command()
def cli():
    click.echo("Hello World")


with open('requirements.txt') as f:
    #all_reqs = f.read().split('\n')
    click.echo(f.read().split('\n'))
#NEED TO INSTALL IPBD import ipdb; ipdb.set_trace()


with open('.gitignore.txt') as giti:
	click.echo(giti.read().split('\n'))


if __name__ == "__main__":
    cli()



import click
from skeleton import output_file_path, read_from_csv_filepath, apply_cleaning_functions, write_to_csv

# function that runs from CLI:
# Command 1: --run [] [] [] : does the damn thing.


@click.command()
def cli():
    click.echo("Hello World")


@click.command()
@click.option('--static', is_flag=True)
def run(static):
    # option that lets you run a pre-populated thing
    if static:
        # use the static path
        # 1. Get the relevant filepath from settings ()
        uncleaned_file_path = 'BudgetREPO/static/Chase9075_recentActivity_static.CSV'
        cleaned_file_path = 'BudgetREPO/static/Chase9075_recentActivity_static_cleaned.CSV'
    else:
        uncleaned_file_path = output_file_path(file_path_of_uncleaned=True)
        cleaned_file_path = output_file_path(file_path_of_uncleaned=False)

    # 2. Read in the csv as a df
    initial_dataframe = read_from_csv_filepath(uncleaned_file_path)

    # 2. Clean the df; add spaces, add columns, add dates etc
    cleaned_dataframe = apply_cleaning_functions(initial_dataframe)

    # 4. Write out to the computer
    write_to_csv(df=cleaned_dataframe, cleaned_file_path=cleaned_file_path)

    # 5. Testing?
    pass


@click.command()
def testing():
	click.echo('Hi!')

# Function that configures a configuration.yaml. 
# TODO: consider removing. No one else will use this code. 
@click.command()
def configure():
    user = click.prompt('What is your username?')
    click.echo("Remember to set your password! We might encrypt with click later.")
    path = click.prompt('What is the filepath?')
    dict = {'auth_userId': user, 'auth_passwd': '', 'filepath': path}
    pass


if __name__ == "__main__":
    run()

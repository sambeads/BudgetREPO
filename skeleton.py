import pandas as pd
import datetime


'''
Things I can do:
	Change the 'amount' columns to positive
	Put in columns with empty strings to make it like my format
	Put in empty rows between dates
'''


def mainer():
    pass

# function that takes the excel file and parses to find the right bits:
# date, amount, description.
# Also inputs 'Chase' as type. Has columns that are empty for type and subtype.
# Leaves some space at the top.


def read_from_excel():
    filepath_of_original_doc = output_file_path(original=True)
    initial_statement = pd.read_csv(
        filepath_of_original_doc)
    # format it a bit
    df = format_input_df(initial_statement)
    
    return write_to_csv(df)

# TODO: This is not good : not supposed to have a boolean in a function statement!
def output_file_path(original=True):
    path = 'C:/Users/sam.beadles/Documents/2_Personal/99_Statements/'
    account = 'Chase9075'
    log = 'RecentActivity'
    time = datetime.datetime.now().strftime("%Y%m%d")
    # the string is Chase9075_RecentActivity_[datetime]
    fstringer = f"{path}{account}_{log}_{time}.csv"
    fstringer_cleaned = f"{path}cleaned_{account}_{log}_{time}.csv"

    if original:
        return fstringer
    else:
        return fstringer_cleaned

def format_input_df(df):
    # take relevant columns
    df_columns = df[['Post Date', 'Amount', 'Description']]
    # add an empty column in position 1
    df_columns.insert(1, '', value=int)
    # Sort by the date
    sorted_df = df_columns.sort_values(by=['Post Date'])

    return sorted_df


def write_to_csv(df):
    path = 'C:/Users/sam.beadles/Documents/2_Personal/'
    folder = '99_Statements/'

    filepath_of_original_doc = output_file_path(original=True)
    filepath_of_cleaned_doc = output_file_path(original=False)

    df.to_csv(filepath_of_cleaned_doc, index=False)


def parsing_excel():
    pass


def read_from_pdf():
    # function that reads from PDF
    pass


def increment(num):
    return num + 1


def broken_increment(num):
    if num == 0:
        return 'zero'
    elif num < 0:
        return 'negative'
    elif num > 1:
        return 'Positive, greater than zero (wrong)'
    else:
        return 'agh!'


if __name__ == '__main__':
    mainer()
    read_from_excel()
    # write_to_csv()

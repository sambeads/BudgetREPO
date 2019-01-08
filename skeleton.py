import pandas as pd
import datetime
import pytest


'''
Things I can do:
    (Done) Change the 'amount' columns to positive
    (Done) Put in columns with empty strings to make it like my format
    (Done) Put in empty rows between dates
    () Ignore scratch
    (Done) Create github
    () Work on CLI command alias
    () Clean up: create docstrings, move functions, refactor and rename
    () Try creating testing for this stuff
    () Figure out how to connect to Chase thru API
    (Done) Take out any identifying information so that my pushes won't show my name
    () Use SSH keys
'''


def output_file_path(file_path_of_uncleaned=True):
    # TODO: This is not good : not supposed to have a boolean in a function statement
    # according to clean code
    path = 'C:/Users/sam.beadles/Documents/2_Personal/99_Statements/'
    account = 'Chase9075'
    log = 'RecentActivity'
    time = datetime.datetime.now().strftime("%Y%m%d")

    # the string is Chase9075_RecentActivity_[datetime]
    fstringer = f"{path}{account}_{log}_{time}.csv"
    fstringer_cleaned = f"{path}cleaned_{account}_{log}_{time}.csv"

    if file_path_of_uncleaned:
        return fstringer
    else:
        return fstringer_cleaned


def read_from_csv_filepath(filepath_of_original_doc):
    initial_statement = pd.read_csv(
        filepath_of_original_doc)
    return initial_statement


def apply_cleaning_functions(unclean_df):
    df_with_all_columns = add_columns_and_sort(unclean_df)
    df_all_cols_new_signage = change_amount_sign(df_with_all_columns)
    df_added_dates_and_spaces = add_spaces_to_dataframe(
        df_all_cols_new_signage)
    return df_added_dates_and_spaces


def add_columns_and_sort(df):
    # Add 'Chase as type'
    df['Marker'] = ''
    df['Subcategory'] = ''
    df['Type'] = ''
    df['Cost'] = df['Amount']
    df['Payment'] = 'Chase'
    df['Empty'] = ''
    df['Date'] = pd.to_datetime(df['Post Date'])
    # take relevant columns
    df_columns = df[['Marker', 'Date', 'Subcategory',
                     'Type', 'Amount', 'Empty', 'Description', 'Payment']]
    # Sort by the date
    sorted_df = df_columns.sort_values(by=['Date'])
    # reset the index
    sorted_df_with_no_index = sorted_df.reset_index(drop=True)

    return sorted_df_with_no_index


def change_amount_sign(df):
    # turn amount to positive
    df['Amount'] = df['Amount'] * -1

    return df


def add_spaces_to_dataframe(df):
    '''

    The reason we have this function is to format empty rows between dates. This is necessary because
    I format my personal Excel budget in this way for readability. 

    It requires a strange flow. I take in a relatively clean dataframe, find all the missing dates,
    and then append the dates onto the original. The append forces Nones in most columns, which 
    prints as empty Excel cells.

    # TODO: figure out how doc strings are really supposed to be written 

    '''
    # First, get the range of dates we're working with in the df
    start_day = df.iloc[1]['Date']
    end_day = df.iloc[-1]['Date']

    # Create a DataTimeSeries of the dates, then convert to frame
    all_dates_in_range = pd.date_range(freq='D', start=start_day, end=end_day)
    all_dates_frame = all_dates_in_range.to_frame()

    # Changing the index of the frame to 1-length of the frame
    length_of_all_dates_frame = len(all_dates_frame)
    all_dates_frame.index = range(length_of_all_dates_frame)

    # Renaming the date column so that the two Date columns align
    all_dates_frame.rename(columns={0: 'Date'}, inplace=True)

    # Combine the two dataframes and sort them
    combined_dates_frame = df.append(all_dates_frame)
    sorted_combined_frame = combined_dates_frame.sort_values(by=['Date'])

    return sorted_combined_frame


def write_to_csv(df, cleaned_file_path):
    df.to_csv(cleaned_file_path, index=False)


if __name__ == '__main__':
    # 1. Get the relevant filepath from settings ()
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


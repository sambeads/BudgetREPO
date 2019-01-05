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
    () Take out any identifying information so that my pushes won't show my name
    () Use SSH keys
'''


def mainer():
    pass

# function that takes the excel file and parses to find the right bits:
# date, amount, description.
# Also inputs 'Chase' as type. Has columns that are empty for type and subtype.
# Leaves some space at the top.


#@pytest.fixture()
def read_from_excel():
    filepath_of_original_doc = output_file_path(original=True)
    initial_statement = pd.read_csv(
        filepath_of_original_doc)
    # format it a bit
    df = format_input_df(initial_statement)
    return df

# TODO: This is not good : not supposed to have a boolean in a function statement!


def add_spaces_to_dataframe(df):
    # single_day_for_comparison = datetime.timedelta(days=1)

    # list_of_separating_dates = []
    # import ipdb; ipdb.set_trace()
    # for i in range((len(df)-1)):
    #     # import ipdb; ipdb.set_trace()
    #     datesMorethanaDayApart = df.loc[i,'Date'] - df.loc[i+1,'Date'] < -single_day_for_comparison
    #     if datesMorethanaDayApart:
    #         list_of_separating_dates = list_of_separating_dates.append(df.loc[i,'Date'])

    # Set the index of the original df and the missing dates df to 'Date'

    # new idea:
    start_day = df.iloc[1]['Date']
    end_day = df.iloc[-1]['Date']

    all_dates_in_range = pd.date_range(freq = 'D',start=start_day, end = end_day)
    
    all_dates_frame = all_dates_in_range.to_frame()

    length_of_all_dates_frame = len(all_dates_in_range.to_frame())
    all_dates_frame.index = range(length_of_all_dates_frame)
    all_dates_frame.rename(columns={0:'Date'},inplace=True)
    combined_dates_frame = df.append(all_dates_frame)
    sorted_combined = combined_dates_frame.sort_values(by=['Date'])

    return sorted_combined


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
    # turn amount to positive
    sorted_df_with_no_index['Amount'] = sorted_df_with_no_index['Amount'] * -1

    return sorted_df_with_no_index


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
    cleaned_dataframe_of_budget_data = read_from_excel()
    spaced_dataframe = add_spaces_to_dataframe(cleaned_dataframe_of_budget_data)
    write_to_csv(spaced_dataframe)

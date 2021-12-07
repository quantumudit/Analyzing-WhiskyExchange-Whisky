# -- Importing Libraries -- #

print('\n')
print('Importing libraries to perform ETL...')

import pandas as pd
import pyfiglet
import warnings

warnings.filterwarnings('ignore')

print('Initiating ETL Process...')
print('\n')

# -- Starting ETL Process --#

etl_title = "WHISKEY DATA ETL"
ascii_art_title = pyfiglet.figlet_format(etl_title, font='small')
print(ascii_art_title)
print('\n')

# -- Connecting to Dataset -- #

print('Connecting to raw dataset')

scraped_data = pd.read_csv("../01_WEBSCRAPING/japanese_whisky_raw_data.csv", index_col=False)

print(f'Shape of scraped dataset: {scraped_data.shape}')
print('\n')

# -- Spliting Column by Delimiter -- #

print('Spliting "volume_alcohol_percentage" by delimiter')

cols_to_add = ['Volume (cl)', 'Alcohol %']
scraped_data[cols_to_add] = scraped_data['volume_alcohol_percentage'].str.split("/", expand=True)

print(f'Shape of dataset after split column operation: {scraped_data.shape}')
print('\n')

# -- Replacing Unnecessary Texts from Columns --#

print('Replacing unnecessary texts in certain columns')

scraped_data['Volume (cl)'] = scraped_data['Volume (cl)'].str.replace('cl', '')
scraped_data['Alcohol %'] = scraped_data['Alcohol %'].str.replace('%', '')
scraped_data['price'] = scraped_data['price'].str.replace('£', '').str.replace(',', '')

print('\n')

# -- Extracting Numeric Value from "reviews_count" Column -- #

print('Extracting numeric value of from "reviews_count" colum with RegEx')

scraped_data['Review Count'] = scraped_data['reviews_count'].str.extract(r'\((\d*).*', expand=False)

print(f'Shape of dataset after text cleaning operations: {scraped_data.shape}')
print('\n')

# -- Removing Unnecessary Columns --#

print('Removing unnecessary columns')

keep_columns = ['whisky_name', 'whisky_type', 'stock_flag', 'description', 'image_url', 'whisky_link', 'ratings','Review Count', 'Volume (cl)', 'Alcohol %', 'price']

whiskey_data = scraped_data[keep_columns]

print(f'Shape of dataframe after removal of unnecessary columns: {whiskey_data.shape}')
print('\n')

# -- Renaming Existing Columns --#

print('Renaming existing columns')

new_column_names = ['Title','Type','Stock Status', 'Description', 'Image Link', 'Details Link','Rating','Review Count','Volume (cl)', 'Alcohol %','Price (£)']
whiskey_data.columns = new_column_names

print(f'New column names in the dataframe: {list(whiskey_data.columns)}')
print('\n')

# -- Adding Custom Index Column -- #

print('Adding custom index column to the dataframe')

custom_index_col = pd.RangeIndex(start=1000, stop=1000+len(whiskey_data), step=1, name='WhiskeyID')

whiskey_data.index = custom_index_col
whiskey_data.index = 'JW' + whiskey_data.index.astype('string')

print(f'Is the index column unique: {whiskey_data.index.is_unique}')
print('\n')

# -- Providing Appropriate DataType to Columns --#

print('Checking the datatype of existing columns:')
print('\n')
print(whiskey_data.info())
print('\n')
print('Providing correct datatype to columns')

# NaN is a float and can't be converted to integer datatype directly; so we have to take the following approach:

whiskey_data['Review Count'] = whiskey_data['Review Count'].astype('float64').astype(pd.Int64Dtype())

# Fixing rest of the columns:

whiskey_data['Volume (cl)'] = whiskey_data['Volume (cl)'].astype('int64')
whiskey_data['Alcohol %'] = whiskey_data['Alcohol %'].astype('float64')
whiskey_data['Price (£)'] = whiskey_data['Price (£)'].astype('float64')

print('Checking datatype of columns after fix:')
print('\n')
print(whiskey_data.info())
print('\n')
print(f'Snippet of the transformed dataframe:')
print('\n')
print(whiskey_data.head())
print('\n')

# -- Exporting Data to CSV File --#

print('Exporting the dataframe to CSV file...')

whiskey_data.to_csv('../03_DATA/japanese_whiskey_data.csv', encoding='utf-8', index_label='WhiskeyID')

print('Data exported to CSV...')
print('ETL Process completed !!!')
"""
    create some fake json book cover records from the book review dataset from kaggle.
    it's a very basic implementation for development - too clean for testing.
"""

import pandas as pd

# read the relevant fields into memory
csv = pd.read_csv('book_reviews.csv', header=0, nrows=500, usecols=['bookID', 'title', 'author'])

# rename the column names from original header to those used in json schema
csv = csv.rename(columns={'bookID': 'bookId'})

# add a placeholder image url
csv['imageUrl'] = pd.Series('https:/didactapp.com/api/images/', index=csv.index)

# add published date values
csv['publishedDate'] = pd.Series('1987-05-01', index=csv.index)

# add description values
csv['description'] = pd.Series('it\'s about space adventures', index=csv.index)

# convert pandas dataframe to json and write to file
json = csv.to_json(path_or_buf='covers.json', orient='records')

"""
    create some fake json book cover records from the book review dataset from kaggle.
    it's a very basic implementation for development - too clean for testing.
"""

import pandas as pd

# read the relevant fields into memory
csv = pd.read_csv('book_reviews.csv', header=0, nrows=500, usecols=['bookID', 'title'])

# rename the column names from original header to those used in json schema
csv = csv.rename(columns={'bookID': 'bookId'})

# add image urls
csv['coverUrl'] = pd.Series('https:/didactapp.com/api/images/', index=csv.index)
csv['thumbnailUrl'] = pd.Series('https:/didactapp.com/api/images/', index=csv.index)

# add date values
csv['publishedDate'] = pd.Series(1520860000, index=csv.index)
csv['revisionDate'] = pd.Series(1520820000, index=csv.index)

# add tagline values
csv['tagLine'] = pd.Series('it\'s about space adventures', index=csv.index)
# add description values
csv['description'] = pd.Series('here\'s what you\'ll learn:', index=csv.index)

# add version number
csv['version'] = pd.Series(2, index=csv.index)

# convert pandas dataframe to json and write to file
json = csv.to_json(path_or_buf='book_list.json', orient='records')

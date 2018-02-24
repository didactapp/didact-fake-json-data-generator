""" an advanced implementation of fake book cover json generation for tests """

import pandas as pd
from datetime import date
import random


def rand_date():
    return str(date(random.randint(1950, 2000), random.randint(1, 12), random.randint(1, 28)))


# read the relevant fields into memory
csv = pd.read_csv('book_reviews.csv', header=0, nrows=10, usecols=['bookID', 'title', 'author', 'review'])

# rename the column names from original header to those used in json schema
csv = csv.rename(columns={'bookID': 'bookId', 'review':'description'})  # use the review column as a fake description
# add a placeholder image url
csv['imageUrl'] = pd.Series('https:/didactapp.com/api/images/', index=csv.index)
# add a randomized date value
csv['publishedDate'] = pd.Series(rand_date(), index=csv.index)
# truncate the description length string to 30 chars (reviews can be long...)
csv['description'] = csv['description'].str[:30]

# convert pandas dataframe to json and write to file
json = csv.to_json(path_or_buf='covers.json', orient='records')

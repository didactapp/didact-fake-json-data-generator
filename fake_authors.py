"""
    create some fake json book cover records from the book review dataset from kaggle.
    it's a very basic implementation for development - too clean for testing.
"""

import pandas as pd

# read the relevant fields into memory
df = pd.read_json('author_list_old.json')  # type:pd.DataFrame

# add first and last name
df['authorId'] = df['bookId']
df['firstName'] = df['author']
df['lastName'] = df['author']
df['about'] = pd.Series('the author is a space ninja', index=df.index)

# remove unneeded cols
df = df.drop('version', axis=1)
df = df.drop('revisionDate', axis=1)
df = df.drop('publishedDate', axis=1)
df = df.drop('tagLine', axis=1)
df = df.drop('title', axis=1)
df = df.drop('coverUrl', axis=1)
df = df.drop('thumbnailUrl', axis=1)
df = df.drop('bookId', axis=1)
df = df.drop('description', axis=1)
df = df.drop('author', axis=1)

# convert pandas dataframe to json and write to file
json = df.to_json(path_or_buf='author_list.json', orient='records')

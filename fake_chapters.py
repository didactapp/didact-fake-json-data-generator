"""
    create some fake json book cover records from the book review dataset from kaggle.
    it's a very basic implementation for development - too clean for testing.
"""

import pandas as pd

# read the relevant fields into memory
df = pd.read_json('book_list.json')  # type:pd.DataFrame

# remove unneeded cols
df = df.drop('version', axis=1)
df = df.drop('revisionDate', axis=1)
df = df.drop('publishedDate', axis=1)
df = df.drop('tagLine', axis=1)
df = df.drop('title', axis=1)
df = df.drop('coverUrl', axis=1)

# add chapterId col
df['chapterId'] = df['bookId']

# reorder cols
cols = df.columns.tolist()
cols[0], cols[-1] = cols[-1], cols[0]
cols[1], cols[-1] = cols[-1], cols[1]
df = df[cols]

# add chapter numbers
df['chapterNum'] = pd.Series(0, index=df.index)

# convert pandas dataframe to json and write to file
json = df.to_json(path_or_buf='chapter_list.json', orient='records')

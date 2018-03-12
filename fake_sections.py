"""
    create some fake json book cover records from the book review dataset from kaggle.
    it's a very basic implementation for development - too clean for testing.
"""

import pandas as pd

# read the relevant fields into memory
df = pd.read_json('chapter_list.json')  # type:pd.DataFrame

# rename col
df['sectionId'] = df['bookId']
df['sectionNum'] = df['chapterNum']

# remove unneeded cols
df = df.drop('thumbnailUrl', axis=1)
df = df.drop('description', axis=1)
df = df.drop('bookId', axis=1)
df = df.drop('chapterNum', axis=1)

# convert pandas dataframe to json and write to file
json = df.to_json(path_or_buf='section_list.json', orient='records')

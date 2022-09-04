import pandas as pd
import random
import math
from tkinter import *

words_df = pd.read_csv("./data/french_words.csv")
# print(words_df.columns)

# print(random.choice(words_df['French']))

# words_dict = words_df.to_dict('index')
# print(words_dict)
# word_dict = {}
#
# for item, row in words_df.iterrows():
#     print(row.English)


# words_dict = {row.French: row.English for (item, row) in words_df.iterrows()}
# print(words_dict)


# for word in words_dict:
#     print(word)
#     print(words_dict[word])

# french_word = (random.choice(list(words_dict)))
# print(french_word)
# print(words_dict[french_word])

# words_dict.pop('partie')
# print(words_dict)

words_df = pd.read_csv("./data/words_to_learn.csv")
print(type(words_df))
# print(words_df)
print(words_df.columns)
#words_dict = {row.French: row.English for (item, row) in words_df.iterrows()}
# print(words_dict)

words_df = pd.read_csv("./data/words_to_learn.csv")
print(type(words_df))
# print(words_df)
print(words_df.columns)
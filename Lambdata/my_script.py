# lambdata/my_script.py

import pandas
import numpy as np
#from sklearn.model_selection import train_test_split

from Lambdata.my_mod import enlarge
from Lambdata.helper import train_val_test_split
from Lambdata.helper import split_dates

print("Welcome to unit 3 Moddule 1!!")

# Datafrme
df = pandas.DataFrame({"X": [1, 5, 10, 15],
                       "c": [2, 6, 8, 10],
                       "y": ['dog', 'cat', 'frog', 'dog'],
                       "Date": ['2010-07-10', '2012-08-20', '2014-09-20', '2016-10-20']
                       })
print(df.head())

# Matrix
target = df["y"]
dates = df["Date"]
features = df.drop(columns="y")

x = 6
print("Enlarge", x, "TO", enlarge(x))

print("Dataframe splits", train_val_test_split(features, target))

print("Dataframe splits dates", split_dates(df, "Date"))

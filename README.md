# cassidyhanna-lambdata

# Installation 

```sh
pip install -i https://test.pypi.org/simple/ cassidy-lambdata

```

# Usage

```py

from Lambdata.my_mod import enlarge

x = 6

print("Enlarge", x, "TO", enlarge(x))


from Lambdata.helper import train_val_test_split

df = pandas.DataFrame({"X": [1, 5, 10, 15],
                       "c": [2, 6, 8, 10],
                       "y": ['dog', 'cat', 'frog', 'dog'],
                       "Date": ['2010-07-10', '2012-08-20', '2014-09-20', '2016-10-20']
                       })
print(df.head())

target = df["y"]
features = df.drop(columns="y")

print("Dataframe splits", train_val_test_split(features, target))


from Lambdata.helper import split_dates

df = pandas.DataFrame({"X": [1, 5, 10, 15],
                       "c": [2, 6, 8, 10],
                       "y": ['dog', 'cat', 'frog', 'dog'],
                       "Date": ['2010-07-10', '2012-08-20', '2014-09-20', '2016-10-20']
                       })
print(df.head())

dates = df["Date"]

print("Dataframe splits dates", split_dates(df, "Date"))

```


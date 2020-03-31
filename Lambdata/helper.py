
from sklearn.model_selection import train_test_split
import pandas as pd


# Train/validate/test split function for a dataframe
# Splitting model data into train, val split sets


def train_val_test_split(X, y, train_size=0.70, val_size=0.15, test_size=0.15,
                         random_state=None, shuffle=True):

    # Split size has to add up to 1
    assert train_size + val_size + test_size == 1

    # first split creates train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    # second splits train into train and val set
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=test_size/(train_size + val_size), random_state=random_state, shuffle=shuffle)

    return X_train, X_val, y_train, y_val, X_test, y_test


# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

def split_dates(df, column):

    df[column] = pd.to_datetime(df[column])
    #df = df.set_index(df[column])

    df['day'] = pd.DatetimeIndex(df[column]).day
    df['month'] = pd.DatetimeIndex(df[column]).month
    df['year'] = pd.DatetimeIndex(df[column]).year
    #df['day'] = df.index.day
    #df['month'] = df.index.month
    #df['year'] = df.index.year

    return df

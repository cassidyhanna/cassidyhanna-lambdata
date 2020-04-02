
from sklearn.model_selection import train_test_split
import pandas as pd


# Train/validate/test split function for a dataframe
# Splitting model data into train, val split sets


def train_val_test_split(X, y, train_size=0.70, val_size=0.15, test_size=0.15,
                         random_state=None, shuffle=True):
    """
    Split arrays or matrices into random train  validation and test subsets

    Param: *arrays sequence of indexables with same length 
      Allowed inputs are lists, numpy arrays, or pandas dataframes.

    train_size: float, int or None, optional (default=0.70)
      default train size is 0.70

    val_size: float, int or None, optional (default=0.15)
        default val size is 0.15

    test_size: float, int or None, optional (default=0.15)
        default test size is 0.15

    random_state: int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator; If RandomState instance, random_state is
        he random number generator; If None, the random number generator is the RandomState instance used by 
        np.random.

    shuffle: boolean, optional (default=True)
        Whether to shuffle the data or not before splitting.

    Returns: DataFrame split DataFrames
    """

    # Split size has to add up to 1
    assert train_size + val_size + test_size == 1

    # first split creates train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    # second splits train into train and val set
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=test_size/(train_size + val_size),
        random_state=random_state, shuffle=shuffle)

    return X_train, X_val, y_train, y_val, X_test, y_test


# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

def split_dates(df, column):
    """
    Splits datas into columns "day", "month" and "year".

    Param: DataFrame and date columns.

    Returns: DataFrame 
    """

    df[column] = pd.to_datetime(df[column])

    df['day'] = pd.DatetimeIndex(df[column]).day
    df['month'] = pd.DatetimeIndex(df[column]).month
    df['year'] = pd.DatetimeIndex(df[column]).year

    return df

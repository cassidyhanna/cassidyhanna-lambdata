
# Lambdata/ helper.py (functional approach)
import pandas
from sklearn.model_selection import train_test_split


# Train/validate/test split function for a dataframe
# Splitting model data into train, val split sets


def train_val_test_split(X, y, train_size=0.70, val_size=0.15, test_size=0.15,
                         random_state=None, shuffle=True):
    """
    Split arrays or matrices into random train, validation and test subsets

    Param: *arrays sequence of indexables with same length
      Allowed inputs are lists, numpy arrays, or pandas dataframes.

    train_size: float, int or None, optional (default=0.70)
      default train size is 0.70

    val_size: float, int or None, optional (default=0.15)
        default val size is 0.15

    test_size: float, int or None, optional (default=0.15)
        default test size is 0.15

    random_state: int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator; If RandomState instance,
        random_state is he random number generator; If None, the random number generator is the
        RandomState instance used by np.random.

    shuffle: boolean, optional (default=True)
        Whether or not the data is shuffled before splitting.

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
    Splits dates into columns "day", "month" and "year".

    Param: DataFrame and date columns.

    Returns: DataFrame
    """
    # Apply datetime function to date column
    df[column] = pandas.to_datetime(df[column])

    # Create day, month and year columns
    df['day'] = pandas.DatetimeIndex(df[column]).day
    df['month'] = pandas.DatetimeIndex(df[column]).month
    df['year'] = pandas.DatetimeIndex(df[column]).year

    return df


# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)
class CustomFrame(pandas.DataFrame):
    """
    param: my-df (pandas.DataFrame) containing a column called "abbrev"
    """

    def add_state_name(self):
        """
         Add corresponding state names to a DataFrame.
        """
        # new_df = self.df.copy()

        names_map = {
            "CA": "Cali",
            "CT": "Conn",
            "CO": "Colorada",
            # todo: more abbrevs!

        }
        self["name"] = self["abbrev"].map(names_map)


if __name__ == "__main__":

    print("---------------")
    df1 = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})

    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(custom_df.head())
    custom_df.add_state_name()
    print(custom_df.head())


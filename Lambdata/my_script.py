# lambdata/my_script.py

import pandas

from Lambdata.my_mod import enlarge

print("Welcome to unit 3 Moddule 1!!")


df = pandas.DataFrame({"X": [1, 2, 3], "y":  [4, 8, 12]})
print(df.head())

x = 6
print("Enlarge", x, "TO", enlarge(x))

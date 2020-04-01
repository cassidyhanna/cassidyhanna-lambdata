# lambdata/my_mod.py


def enlarge(n):
    """
    Multiplies a number by 100 

    Param: n (numeric) the number to enlarge

    Return the enlarged number (numeric)
    """
    return n * 100


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))

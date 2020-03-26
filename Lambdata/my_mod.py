# lambdata/my_mod.py


def enlarge(n):
    return n * 100


if __name__ == "__main__":

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("PLEASE INPUT A NUMBER TO ENLARGE: "))
    print(enlarge(y))

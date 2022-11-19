from groups.Zn import Zn
from tabulate import tabulate


def main():

    z16 = Zn(16)
    z15 = Zn(15)

    # print(f"order of Z16: {z16.order}")
    # print(f"order of Z15: {z15.order}")

    z16.cayley()
    




if __name__ == "__main__":
    main()
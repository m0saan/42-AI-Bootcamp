import sys


def operations(n1: int, n2: int) -> str:
    quotient = ""
    remainder = ""

    sum = n1 + n2
    diff = n1 - n2
    product = n1 * n2
    if n2 == 0:
        quotient = "ERROR (div by zero)"
        remainder = "ERROR (modulo by zero)"
    else:
        quotient = n1 / n2
        remainder = n1 % n2
    return """    Sum:         {}
    Difference:  {}
    Product:     {}
    Quotient:    {}
    Remainder:   {}""".format(sum, diff, product, quotient, remainder)


if __name__ == '__main__':
    strHelp = """Example:
    python operations.py 10 3"""
    if len(sys.argv) == 1:
        print(strHelp)
    elif len(sys.argv) > 3:
        print("InputError: too many arguments")
    elif len(sys.argv) == 3 and (not sys.argv[1].isdecimal() or not sys.argv[2].isdecimal()):
        print("InputError: only numbers")
        print(strHelp)
    else:
        print(operations(int(sys.argv[1]), int(sys.argv[2])))

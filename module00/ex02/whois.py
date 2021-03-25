import sys


def whois(n: int) -> str:
    if n == 0:
        return "I'm Zero."
    elif n % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if not arg.isnumeric() or len(sys.argv) > 2:
            print("ERROR")
        else:
            print(whois(int(sys.argv[1])))

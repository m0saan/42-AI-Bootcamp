import sys


def reverse(string: str) -> str:
    for index, char in enumerate(string):
        if char.isupper():
            char = string[index].lower()
        else:
            char = string[index].upper()
    return string[::-1]

    return string[::-1]


if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        print(reverse(sys.argv[i]), end=" ")

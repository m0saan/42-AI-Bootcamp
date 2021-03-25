import sys


def filter_words(s: str, n: int) -> list:
    punctuation_marks = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    for ch in s:
        if ch in punctuation_marks:
            s = s.replace(",", "")
    words = s.split(" ")
    ls = [word for word in words if len(word) > n and word not in punctuation_marks]
    return ls


if __name__ == '__main__':
    if len(sys.argv) != 3 or (type(sys.argv[1]) != str) or (type(sys.argv[2]) != int):
        print("ERROR")
    else:
        print(filter_words(sys.argv[1], int(sys.argv[2])))

from random import randint


def generator(text: str, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""

    if type(text) is not str:
        print("ERROR")
        return

    ls_text = text.split(sep)

    if option is not None:
        if option == "shuffle":
            n = len(ls_text)
            for i in range(n + 1):
                _shuffle(i, ls_text, n)

        elif option == "unique":
            s = set()
            for item in ls_text:
                s.add(item)
            ls_text = list(s)
        elif option == "ordered":
            ls_text.sort()

    for item in ls_text:
        yield item


def _shuffle(i, ls_text, n):
    change = i + randint(0, n - i)
    if change < len(ls_text):
        swap(ls_text, i, change)


def swap(ls: list, i, change):
    tmp = ls[i]
    ls[i] = ls[change]
    ls[change] = tmp


txt = "Le Lorem Ipsum Ipsum du faux du texte."
for word in generator(txt, sep=" ", option="unique"):
    print(word)

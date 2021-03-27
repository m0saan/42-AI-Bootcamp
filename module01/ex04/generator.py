from random import randint


def generator(text: str, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""

    if type(text) is not str:
        print("ERROR")
        return

    ls_text = text.split(sep)
    s = set()

    if option is not None:
        if option == "shuffle":

        elif option == "unique":
            for item in ls_text:
                s.add(item)
            ls_text = list(s)
        elif option == "ordered":
            ls_text.sort()

    for item in ls_text:
        yield item


txt = 1.0
for word in generator(txt, sep=" ", option="unique"):
    print(word)


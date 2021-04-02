def what_are_the_vars(*args, **kwargs) -> object:
    """Your code"""
    o = ObjectC()
    if not len(args) and not len(kwargs):
        return o

    s = "var_"
    var_counter = 0
    vars_set = set()
    for item in args:
        o.__setattr__(s + str(var_counter), item)
        vars_set.add(s + str(var_counter))
        var_counter += 1

    for k, v in kwargs.items():
        if k in vars_set:
            return None
        o.__setattr__(k, v)

    return o


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

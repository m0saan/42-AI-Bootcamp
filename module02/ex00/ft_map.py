def ft_map(function_to_apply, list_of_inputs):
    res = []
    for item in list_of_inputs:
        res.append(function_to_apply(item))
    return res


ls = [
    ("product1", 12),
    ("product2", 10),
    ("product3", 22),
    ("product4", 42),
    ("product5", 19),
]

s = "Hello World."


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)
squared = ft_map(square, numbers)
print(squared)

print(ft_map(lambda item: item.isupper(), s))
print(list(map(lambda item: item.isupper(), s)))

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = list(map(int, str_nums))
print(int_nums)
int_nums = ft_map(int, str_nums)
print(int_nums)

numbers = [-2, -1, 0, 1, 2]

print("original map: ", list(map(abs, numbers)))
print("ft_map: ", ft_map(abs, numbers))

print("original map: ", list(map(float, numbers)))
print("ft_map: ", ft_map(float, numbers))

words = ["Welcome", "to", "Real", "Python"]

print("original map: ", list(map(len, words)))
print("ft_map: ", ft_map(len, words))


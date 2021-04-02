from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    """ ft_reduce() implements reduction. Reduction is when you reduce a list of items to a
    single cumulative value. """
    if not len(list_of_inputs):
        raise ValueError("ft_reduce() of empty sequence with no initial value")
    it = iter(list_of_inputs)
    ans = next(it)
    for item in it:
        ans = function_to_apply(ans, item)
    return ans


def add(a, b):
    result = a + b
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("ft_reduce: ", ft_reduce(add, numbers))
print("reduce: ", reduce(add, numbers))

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("ft_reduce: ", ft_reduce(lambda a, b: a + b, numbers))
print("reduce: ", reduce(lambda a, b: a + b, numbers))

print("ft_reduce: ", ft_reduce(lambda a, b: a * b, numbers))
print("reduce: ", reduce(lambda a, b: a * b, numbers))

numbers = [1]

print("ft_reduce: ", ft_reduce(lambda a, b: a * b, numbers))
print("reduce: ", reduce(lambda a, b: a * b, numbers))

numbers = [1, 2, 3, 4]

print("ft_reduce: ", ft_reduce(lambda a, b: a * b, numbers))
print("reduce: ", reduce(lambda a, b: a * b, numbers))


numbers = []

# Will raise a value error exception with passed an empty list.
print("ft_reduce: ", ft_reduce(lambda a, b: a * b, numbers))
print("reduce: ", reduce(lambda a, b: a * b, numbers))

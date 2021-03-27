def ft_filter(function_to_apply, list_of_inputs):
    return [item for item in list_of_inputs if function_to_apply(item)]


# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter in vowels:
        return True
    else:
        return False


print(list(filter(filter_vowels, letters)))
print(ft_filter(filter_vowels, letters))

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
print("original filter: ", list(filter(lambda x: x % 2 != 0, seq)))
print("ft_filter: ", ft_filter(lambda x: x % 2 != 0, seq))

# result contains even numbers of the list
print("original filter: ", list(filter(lambda x: x % 2 == 0, seq)))
print("ft_filter: ", ft_filter(lambda x: x % 2 == 0, seq))
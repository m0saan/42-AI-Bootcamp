from string import punctuation

def text_analyzer(*s) -> str:
    """ This function counts the number of upper characters, lower characters, punctuation and spaces in a given
    text. """

    if len(s) == 0:
        print("What is the text to analyse?")
        s = input()
    elif len(s) > 1:
        print("ERROR")
        return
    elif len(s) == 1:
        s = s[0]

    chars_sum = 0
    upper_letters_sum = 0
    lower_letters_sum = 0
    punctuation_marks_sum = 0
    spaces_sum = 0

    for char in s:
        if char.isupper():
            upper_letters_sum += 1
        elif char.islower():
            lower_letters_sum += 1
        elif char.isspace():
            spaces_sum += 1
        elif char in punctuation:
            punctuation_marks_sum += 1
        chars_sum += 1

    print("The text contains {} characters: \n - {} upper letters \n - {} lower letters \n - {} punctuation marks \n -"
          " {} spaces \n".format(chars_sum, upper_letters_sum,
                                 lower_letters_sum, punctuation_marks_sum, spaces_sum))


text_analyzer("dfsd!!  ")
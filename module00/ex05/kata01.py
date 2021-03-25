languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

s = """{} was created by {}
{} was created by {}
{} was created by {}""".format('Python', languages.get('Python'), 'Ruby', languages.get('Ruby'), 'PHP', languages.get('PHP'))

print(s)
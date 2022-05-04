def accum(s):
    string = []
    for count, letter in enumerate(s):
        string.append(letter.upper() + letter.lower()*(count))
    return '-'.join(string)
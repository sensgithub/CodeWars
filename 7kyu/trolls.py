def disemvowel(string):
    _string = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in string:
        if vowel in vowels:
            continue
        _string += vowel
    string = _string
    return string
def get_count(sentence):
    vowels = set("aeiou")
    count = 0

    for i in sentence:
        if i in vowels:
            count += 1
    return count
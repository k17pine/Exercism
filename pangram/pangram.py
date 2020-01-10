import string


def is_pangram(sentence):
    letters = string.ascii_lowercase
    for i in sentence:
        letters = letters.replace(i.lower(), '')
    if len(letters) == 0:
        return True
    else:
        return False

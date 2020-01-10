import random
from random import randint
import string


def generate():
    first = ''.join(random.sample(string.ascii_uppercase, 2))
    second = ''.join(random.sample(string.digits, 3))
    return first + second


class Robot:

    def __init__(self):
        self.name = generate()
        names.extend(self.name)

    def reset(self):
        while True:
            if generate() not in names:
                self.name = generate()
                names.extend(self.name)
                return 0


names = []

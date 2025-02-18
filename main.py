# source venv/bin/activate

import math


class Dog:
    def __init__(self, breed):
        self.breed = breed


mutt = Dog("Mutt")
poodle = Dog("Poodle")

print(mutt.breed)
print(poodle.breed)


import random

class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def gender(self):
        try:
            # If it has been defined for the instance, simply return the gender
            return self._gender
        except AttributeError:
            # If it's not defined yet, define it, and then return it
            self._gender = random.choice(['male', 'female'])
            return self._gender

r = Person('rachel')
s = Person('Stanky')
print(r.gender)
print(s.gender)
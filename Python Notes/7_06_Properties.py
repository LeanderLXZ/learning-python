# Properties


# Properties provide a way of customizing access to instance attributes.
# They are created by putting the property decorator above a method.
# When the instance attribute with the same name as the method is accessed, the method will be called instead.
# One common use of a property is to make an attribute read-only.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):       # read-only
        return False

pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)
print('\n')

# pizza.pineapple_allowed = True
# AttributeError: can't set attribute


# Properties can also be set by defining setter/getter functions.
'''
    setter - sets the corresponding property's value
    getter - gets the value
'''
# Use a decorator of the same name as the property, followed by a dot and the setter/getter keyword.

class Pie:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input('Enter the password: ')
            if password == '123':
                self._pineapple_allowed = value
            else:
                raise ValueError('Alert! Intruder!')

pie = Pie(['cheese', 'tomato'])
print(pie.pineapple_allowed)
pie.pineapple_allowed = True
print(pie.pineapple_allowed)


# Example

class Student(object):
    def __init__(self, score, birth):
        self._score = score
        self._birth = birth

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):                   # read-only
        return 2014 - self._birth

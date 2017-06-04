# Magic Methods

import random

# Magic methods are special methods which have double underscores at beginning and end of their names.
# Also known as dunders.


# Operator overloading
# Defining operators for custom classes that allow operators such as + and * \
# to be use on them.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

a = Vector2D(5, 7)
b = Vector2D(3, 9)

c = a + b
print(c.x, c.y)
print('\n')


# Magic Methods
'''
    __add__ : +
    __sub__ : -
    __mul__ : *
    __truediv__ : /
    __floordiv__ : //
    __mod__ : %
    __pow__ : **
    __and__ : &
    __xor__ : ^
    __or__ : |
    __lt__ : <
    __le__ : <=
    __eq__ : ==
    __ne__ : !=
    __gt__ : >
    __ge__ : >=
'''

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
eggs = SpecialString("eggs")

print(spam/hello)
print('\n')
spam > eggs
print('\n')


# Magic Methods
'''
    __len__ : len()
    __getitem__ : indexing
    __setitem__ : assigning to indexed values
    __delitem__ : deleting indexed values
    __iter__ : iteration over objects (e.g., in for loops)
    __contains__ : in
    __call__ : calling objects as functions
    __int__ : converting objects to int type
    __str__ : converting objects to string type
'''

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, item):
        return self.cont[item + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


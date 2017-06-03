# Data Hiding


# Weakly private methods and attributes
# Have a single underscore at the beginning.
# It's mostly only a convention and does not stop external code from accessing them.
# Actual effect: from module_name import * won't import variables that start with a single underscore.

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])

print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
print('\n')


# Strongly private methods and attributes
# Have a double underscore at the beginning.
# This causes their name to be mangled, which means that they can't be accessed from outside the class.
# Name mangled method can still be accessed externally by a different name.
# The method __privatemethod of class Spam could be acssesed externally with _Spam__privatemethod.

class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()

print(s._Spam__egg)
# print(s.__egg)
# AttributeError: 'Spam' object has no attribute '__egg'

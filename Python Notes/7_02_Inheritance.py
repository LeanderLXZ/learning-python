# Inheritance

# Inheritance ---- provides a way to share functionality between classes.
# To inherit a class from another class, put the superclass name in parentheses after the class name.
'''
    subclass   - a class that inherits from another class.
    superclass - a class that is inherited from.
'''

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
print('\n')


# If a class inherit from another with the same attributes or methods, it overrides them.

class Wolf:  # superclass
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):  # subclass
    def bark(self):
        print("Woof!")

husky = Dog("Max", "grey")
husky.bark()
print('\n')


# Inheritance can be indirect.
# Circular inheritance is not possible.

class A:
    def method(self):
        print("A method")


class B(A):
    def another_mothod(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_mothod()
c.third_method()
print('\n')


# super ---- a useful inheritance-related function.
#            It can be used to find the method with a certain name in an object's superclass.

class D:
    def spam(self):
        print(1)


class E(D):
    def spam(self):
        print(2)
        super().spam()

E().spam()

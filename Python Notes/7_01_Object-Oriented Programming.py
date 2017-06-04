# Object-Oriented Programming
'''
    Class  - describes what the object will be, but is separate from the object itself.
             You can use the same class as a blueprint for creating multiple different objects.
    Method - functions in class.
'''
class Cat:
    def __init__(self, color, legs):  # define a class named Cat, which has two attributes: color and legs
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


# __init__ ---- the class constructor
# The most important method in a class.
# This is called when an instance(object) of the class is created, using the class name as a function.
# self ---- All methods must have self as their first parameter.
# attribute ---- Instances of a class have attributes, which are pieces of data associated with them.
print(felix.color)
print(stumpy.legs)
print('\n')


# Classes can have other methods defined to add functionally to them.
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "browm")
print(fido.name)
fido.bark()
print('\n')

class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi from " + self.name)

stu = Student("Leander")
stu.sayHi()
print('\n')

# Class attribute ---- created by assigning varibles within the body of the class.
#                      It can be accessed either from instances of the class, or the class itself.
class Dog1:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog1("Fido", "browm")
print(fido.legs)
print(Dog1.legs)


# AttributeError ---- Trying to access an attribute or method of an instance that isn't defined.


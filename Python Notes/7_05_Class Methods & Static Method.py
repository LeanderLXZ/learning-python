# Class Methods & Static Method


# Class Methods
'''
    Class Methods  - Called by a class, which is passed to the 'cls' parameter of the method.
    Objects Method - Called by an instance of a class, which is passed tp the 'self' parameter of the method.
'''
# Marked with a classmethod decorator.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
print('\n')


# Static Methods

# They don't receive any additional arguments.
# They are identical to normal functions that belong to a class.
# Marked with a staticmethod decorator.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
print(pizza.toppings)
print('\n')


# Example


class Person:
    def __init__(self):
        print("init")

    @staticmethod
    def say_hello(hello):
        if not hello:
            hello = 'hello'
        print("I will say %s" % hello)

    @classmethod
    def introduce(cls, hello):
        cls.say_hello(hello)
        print("from introduce method")

    def hello(self, hello):
        self.say_hello(hello)
        print("from hello method")

Person.say_hello("HaHa")
Person.introduce("Hello world!")
# Person.hello("Hello")
# TypeError: hello() missing 1 required positional argument: 'hello'

print("*" * 20)
p = Person()
p.say_hello("HaHa")
p.introduce("Hello world!")
p.hello("hello")

def my_func():
    print("spam")

my_func()


def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
print('\n')


def print_sum_twice(x, y):
    print(x + y)
    print(x + y)

print_sum_twice(5, 8)
print('\n')


def max(x, y):
    if x>= y:
        return x
    else:
        return y
print(max(4, 7))
z = max(8, 5)
print(z)
print('\n')


# Functions can be assigned and reassigned to variables.
def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))
print('\n')


# Functions can be used as arguments of other functions.
def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
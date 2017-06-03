# A key part of functional programming is higher-order functions
# Higher-order functions take other functions as arguments, or return them as results.
def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5

print(apply_twice(add_five, 7))


# Functional programming seeks to use pure functions. ---- Return a value that depends only on their arguments.
# Pure function:
def pure_func(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# Impure function: ---- Don't do that.
some_list = []


def impure_func(arg):
    some_list.append(arg)

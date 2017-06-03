# Recursion

# The fundamental part of recursion is self - reference - functions calling themselves.


def factorial(x):
    if x == 1:
        return 1  # base case
    else:
        return x * factorial(x - 1)

print(factorial(5))

# Result in RuntimeError when forget to implement the base case.
# def factorial(x):
#     return x * factorial(x - 1)
#
# print(factorial(5))

# Recursion can be indirect.
# One function can call a second, which calls the first.
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(17))
print(is_odd(22))
print(is_even(22))

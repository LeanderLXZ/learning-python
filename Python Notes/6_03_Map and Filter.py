import numpy as np


# map

# Function map takes a function and an iterable as arguments,
# and returns a new iterable with the function applied to each argument.

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# use lambda
print(list(map(lambda x: x + 5, nums)))


# filter

# Function filter filters an iterable by removing items that don't match a predicate(a function that returns a Boolean).

res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

strings = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
print(nums[:-1])
print(list(map(lambda x: x[:-1], strings)))

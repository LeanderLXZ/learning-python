# Itertools

# Itertools is a standard library that contains several functions that are useful in functional programming.

from itertools import count
from itertools import accumulate, takewhile
from itertools import product, permutations

# Infinite iterators
# count ---- counts up infinitely from a value.
# cycle ---- infinitely iterates through an iterable (for instance a list or string).
# repeat ---- repeats an object, either infinitely or a specific number of times.

for i in count(3):
    print(i)
    if i >= 11:
        break
print('\n')


# Operate on iterables
# takewhile ---- takes items from an iterable while a predicate function remains true.
# chain ---- combines several iterables into a long one.
# accumulate ---- returns a running total of values in an iterable.

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))
print('\n')

# Combinatoric functions
# product, permutation ---- show all possible combinations of some items.

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

a = list(product(letters, range(2)))
b = list(permutations(letters))
print(a[0][1])
print(b[1])  # ---- tuple

c = {1, 2}
d = {2, 3, 7}
print(list(product(range(3), c)))
print(list(product(c, d)))

# Sets

num_set = {1, 3, 4, 5}
word_set_1 = {"spam", "eggs", "sausage"}
word_set_2 = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print(word_set_1)
print(word_set_2)
print("spam" in word_set_1)

# Create an empty set
my_set = set()
# Create an empty dictionary
dict = {}

# Sets are unordered, which means they cannot be indexed.
# They cannot contain duplicate elements.

# Method
'''
    add    - add an element to a set.
    remove - remove a specific element from a set.
    pop    - remove an arbitrary element from a set.
'''
my_set.add("spam")
num_set.remove(3)
word_set_1.pop()

print(my_set)
print(num_set)
print(word_set_1)
print('\n')

# Sets can be combined using mathematical operations.
'''
    | - Union operator combines two sets from a new one containing items in either.
    & - Intersection operator gets items only in both.
    - - Difference operator gets items in the first set but not in the second.
    ^ - Symmetric difference operator gets items in either set, but not both.
'''

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

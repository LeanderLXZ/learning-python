# Generators


# Generators are a type of iterable.
# They don't allow indexing with arbitrary indices, but they can be iterated through for loops.

def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


# Generators don't have the memory restrictions of lists.
# They can be infinite.
def infinite_sevens():
    while True:
        yield 7

# for i in infinite_sevens():
#     print(i)


def get_even():
    num = 2
    while True:
        if num % 2 == 0:
            yield num
        num += 1

# for i in get_even():
#     print(i)


# Finite generators can be converted into lists by passing them as arguments to the list function.
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))


def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word

print(list(make_word()))
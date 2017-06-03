# List Slices
square = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(square[2:6])
print(square[3:8])
print(square[0:1])
print(square[:7])
print(square[7:])
print('\n')

sq = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
print(sq[2:6])
print(sq[:7])
print(sq[7:])
print('\n')

print(square[::2])
print(square[::3])
print(square[2:8:3])
print('\n')

print(square[1:-1])
print(square[2:-3])
# Using [::-1] to reverse a list.
print(square[::-1])
print(square[7:5:-1])
print('\n')

# List Comprehensions
cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
print('\n')

# even = [2*i for i in range(10**100)] ---- result in a MemoryError


# List Functions
# all and any ---- take a list as an argument, and return True if all or any (respectively) of
# their arguments evaluate to True (and False otherwise)
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
if __name__ == '__main__':
    if any([i % 2 == 0 for i in nums]):
        print("At least one is even")

# enumerate ---- iterate through the values and indices of a list simultaneously.
for v in enumerate(nums):
    print(v)

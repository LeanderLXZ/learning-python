words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])
print('\n')

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
print('\n')

my_str = "Hello world!"
print(my_str[6])
print('\n')

nums = [1, 2, 3]
nums[2] = 5
print(nums)
print(nums + [4, 5, 6])
print(nums * 3)
print('\n')

print("Hello" in words)
print("world" not in words)
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
print('\n')

# list Functions
# list.append() ---- Add an item to the end of an existing list.
nums.append(4)
print(nums)
# len(list) ---- Get the number of items in a list.
print("The length of 'nums' is " + str(len(nums)))
print('\n')

# list.insert() ---- Insert a new item at any position in the list.
nums.insert(2, "a number")
print(nums)
print('\n')

# list.index() ---- Find the first occurrence of a list item and return its index.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
# print(letters.index('z')) ----- ValueError: 'z' is not in list
print('\n')


# range
# range() ---- Create a sequential list of numbers.
numbers_1 = list(range(10))
print(numbers_1)

numbers_2 = list(range(3, 8))
print(numbers_2)
print(len(numbers_2))
print(range(20) == range(0, 20))

numbers_3 = list(range(5, 20, 2))
print(numbers_3)
numbers_4 = list(range(3, 15, 3))
print(numbers_4)

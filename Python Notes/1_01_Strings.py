# String Formatting
# Each arguments of the format function is placed in the string at the corresponding position, which is
# determined using the curly braces {}.
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
print("{0}{1}{0}".format("abra", "cad"))
print("{x}, {y}".format(x=5, y=12))
print('\n')

a = 20
b = "apple"
c = "pen"
print("{0} {1}".format(a, b))
print("{x} {y} {z}".format(x=a, y=b, z=c))
print("{b} {a} {c}".format(b=a, a=c, c=b))
print('\n')

# String Functions
# join ---- joins a list of strings with another string as a separator.
print(", ".join(["spam", "eggs", "ham"]))

# replace ---- replaces one substring in a string with another.
print("Hello ME".replace("ME", "world"))

# startswith and endswith ---- determine if there is a substring at the start and end of a string, respectively.
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))

# lower and upper ---- change the case of a string.
print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE.".lower())

# split ---- turns a string with a certain separator into a list.
print("spam, eggs, ham".split(", "))

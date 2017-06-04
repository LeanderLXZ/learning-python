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
'''
    join       - joins a list of strings with another string as a separator.
    replace    - replaces one substring in a string with another.
    startswith - determine if there is a substring at the start  of a string.
    endswith   - determine if there is a substring at the end of a string.
    lower      - change the string to be lower case.
    upper      - change the string to be upper case.
    split      - turns a string with a certain separator into a list.
'''

print(", ".join(["spam", "eggs", "ham"]))
print("Hello ME".replace("ME", "world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE.".lower())
print("spam, eggs, ham".split(", "))

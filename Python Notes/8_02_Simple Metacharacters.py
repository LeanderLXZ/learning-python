# Simple Metacharacters


import re

# Raw string
raw_str = r'I am \r\a\w'

print(raw_str)


# Metacharacters
'''
    . - matches any character, other than a new line
    ^ - matches the start of a string
    $ - matches the end of a string
'''

pattern1 = r'gr.y'
pattern2 = r'^gr.y$'

if re.match(pattern1, 'grey'):
    print('1 Match pattern1')

if re.match(pattern1, 'gray'):
    print('2 Match pattern1')

if re.match(pattern1, 'blue'):
    print('3 Match pattern1')

if re.match(pattern2, 'grey'):
    print('4 Match pattern2')

if re.match(pattern2, 'gray'):
    print('5 Match pattern2')

if re.match(pattern2, 'stingray'):
    print('6 Match pattern2')

if re.match(pattern1, 'stingray'):
    print('6 Match pattern1')




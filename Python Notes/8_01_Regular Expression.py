# Regular Expression Introduction

# Regular expression can be accessed using the 're' module.
'''
    re.match   : function - be use to determine whether it matches at the beginning of a string.
                 If it does, it returns an object representing the match, if not, it returns None.
    re.search  : function - finds a match of pattern anywhere in the string.
    re.findall : function - returns a list of all substring that match a pattern.
'''

# Use raw strings as r'expression' to avoid confusion.

import re

pattern = r'spam'

if re.match(pattern, 'spamspamspam'):
    print('Match')
else:
    print('No match')

if re.match(pattern, 'eggspamsausagespam'):
    print('Match')
else:
    print('No match')

if re.search(pattern, 'eggspamsausagespam'):
    print('Match')
else:
    print('No match')

print(re.findall(pattern, 'eggspamsausagespam'))
print('\n')


# method of match
'''
    group - returns the string matched
    start - returns the start position of the first match
    end   - returns the end position of the first match
    span  - returns the start and end positions of the first match as a tuple
'''

pattern = r'pam'

match = re.search(pattern, 'eggspamsausage')
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    print('\n')


# Search and replace

# re.sub(pattern, repl, string, max=0)

# method - replaces all occurrences of the pattern in string with repl, \
# substituting all occurrences, unless max provided
# returns the modified string.

str = 'My name is David. Hi David.'
pattern = r'David'
newstr = re.sub(pattern, 'Amy', str)
print(newstr)
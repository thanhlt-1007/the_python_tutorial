### 3.1.2. Text

# Reference: https://docs.python.org/3/tutorial/introduction.html#text

"""
Python can manipulate text (represent by type str, so-called "strings") as well as numbers.
This includes
- characters "!"
- words "rabbit"
- names "Paris"
- sentences "Got your back.",
- etc Yay! :)".
They can be enclosed in single quotes ('...') or double quotes ("...") with the same result.
"""

print("3.1.2. Text")

# single quotes
print('spam eggs')

# double quotes
print("Paris rabbit got your back :)! Yay!")

# digits and numerals enclosed in quotes are also strings
print('1975')

"""
To quote a quote,
we need to "escape" it, by preceding it with \.
Alternatively, we can use the other type of quatation marks.
"""

# use \' to escape the single quote ...
print('doesn\'t')

# ... or use double quote instead
print("doesn't")
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

"""
In the Python shell,
the string definition and output string can look different.
The print() function produces a more readable output,
by omitting the enclosing quotes and by printing escaped and special characters:
"""

# \n means newline
s = 'First line.\nSecond line.'

# without print(), special characters are included in the string
# 'Furst line.\nSecond line.'
s

# with print(), special characters are interpreted, so \n produces new line
# First line.
# Second line.
print(s)

"""
If you don'w eant characters prefaced by \ to be interpretered as special characters,
you can use raw strings by adding an r before the first quote:
"""

# here \n means newline!
print('C:\some\name')
# C:\some
# ame

# note the r before the quote
print(r'C:\some\name')
# C:\some\name

"""
String literals can span multiple lines.
One way is using tripe-quotes \"""...\""" or '''...'''.
End of lines are automatically included in the string, but it's possible to prevent by adding a \ at the end of line.
The follow example:
"""

print("""\
Usage: thingy [OPTIONS]
  - h           Display this usage message
  - H hostname  Hostname to connect to
""")

"""
Strings can be concatenated (glued together) with the + operator,
and repeated with *
"""

# 3 times "un", followed by "ium"
print(3 * "un" + "ium")
# unununium

"""
Two or moew string literals (i.e the ones enclosed between quotes) next to each other are automatically concatenated.
"""
print("Py" "thon")
# "Python"

"""
This feature is particolarly useful when you want to break long strings:
"""

text = ('Put several strings within parentheses'
        'to have them joined together.')
print(text)

"""
This only works with two literals though, not with a variables or expressions:
"""

prefix = "Py"

# try:
#   prefix "thon"
# except Exception as exception:
#   print("exception:", exception)
#
# SyntaxError: invalid syntax
#

"""
If you want to concatenated variables or a variable and a literal, use +
"""

print(prefix + "thon")

"""
Strings can be indexed (subscripted),
with the first character having index 0.
There is no separate character type;
a character is simply a string of size one:
"""

word = "Python"
print("word:", word)

# character in position 0
print("word[0]:", word[0])

# character in position 5
print("word[5]:", word[5])

# last character
print("word[-1]:", word[-1])

# second-last character
print("word[-2]:", word[-2])

print("word[-6]:", word[-6])

"""
Note that since -0 uis the same as 0,
negative indices start from -1.

In addtion to indexing,
slicing is also supported.
While indexing is used to obtain individual characters,
slicing allows you to obtain a substring
"""

# characters from position 0 (included) to 2 (excluded)
print("word[0:2]:", word[0:2])

# characters from position 2 (included) to 5 (excluded)
print("word[2:5]", word[2:5])

"""
Since indices have useful defaults;
an omitted first index defaults to zero,
an omitted second index defaults to the size of the string being sliced.
"""

# character from the beginning to position 2 (excluded)
print("word[:2]:", word[:2])

# characters from position 4 (included) to the end
print("word[4:]:", word[4:])

# characters from the second-last (included) to the end
print("word[-2:]:", word[-2:])

"""
Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s
"""

print("word[:2] + word[2:]:", word[:2] + word[2:])
print("word[:4] + word[4:]:", word[:2] + word[2:])

"""
Attempting to use an index that us too large will result in an error
"""

print("Attempting to use an index that us too large will result in an error")

try:
  word[42]
except Exception as exception:
  print(exception)

"""
However, out of range slice indexes are handled gracefully when used for slicing:
"""

print("word[4:42]:", word[4:42])
print("word[42:]:", word[42:])

"""
Python strings cannot be changed - they are immutable.
Therefore, assigning to an indexed position in the string results in an error:
"""

print("""
  Python strings cannot be changed - they are immutable.
  Therefore, assigning to an indexed position in the string results in an error:
""")

try:
  word[0] = "J"
except Exception as exception:
  print(exception)

try:
  word[2:] = "J"
except Exception as exception:
  print(exception)

"""
If you need a different string, you should create a new one:
"""

print("'J' + word[1:]:", 'J' + word[1:])
print("word[:2] + 'py':", word[:2] + 'py')

"""
The built-in function len returns the length of a string:
"""

s = "supercalifragilisticexpialidocious"
print("len(s):", len(s))

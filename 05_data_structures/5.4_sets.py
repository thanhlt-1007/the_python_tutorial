## 5.4. Sets

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#sets

"""
Python also includes a data types for sets. A set is an unordered collection with no duplicate elements.
Basic ises include membership testing and eliminating duplicate entries.
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets.
Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in  the next section.

Here is a brief demonstration:
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket:", basket)

print("'orange' in basket:", 'orange' in basket)
print("'crabgrass' in basket:", 'crabgrass' in basket)

"""
Demonstrate set operations on unique letters from two words
"""

# unique letters in a
a = set('abracadabra')
print("a:", a)

# unique letters in b
b = set('alacazam')
print("b:", b)

# letters in a but not in b
print("a - b:", a - b)

# letters in a or b or both
print("a | b:", a | b)

# letters in both a and b
print("a & b:", a & b)

# letters in a or b but not both
print("a ^ b:", a ^ b)

"""
Similarly to list comprehensions, set comprehensions are also supported:
"""

a = { x for x in 'abracadabra' if x not in 'abc'}
print("a:", a)

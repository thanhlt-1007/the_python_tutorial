## 5.5. Dictionaries

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#dictionaries

"""
Another useful data type built into Python is the dictionary.
Dictionaries are some-times found in other languages as "associative memories" or "associative arrays".
Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type;
strings and numbers can always be keys.
Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
You can't ise lists as kets, sunce lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

It is best to think of a dictionary as a set of key: value paris, with the requirement that they keys are unique (within one dictionary).
A pair of braces creates an empty dictionary: {}.
Placing a comma-seperated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key.
It is also possible to delete a key:value pair with del.
If you store using a key that is already in use, the old value associated with that key is forgetten.
It is an error to extracyt a value using a non-existent key.

Performing list(d) on a dictionary returns a list of all they keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead).
To check whether a single key is in the dictionary, use the in keyword.

Here is a small example using a dictionary
"""

tel = {"jack": 4098, "sape": 4139}
print("tel:", tel)

tel["guido"] = 4127
print("tel:", tel)

print("tel['jack']:", tel["jack"])

del tel["sape"]
print("tel:", tel)

tel["irv"] = 4127
print("tel:", tel)

print("list(tel):", list(tel))

print("sorted(tel):", sorted(tel))

print("'guido' in tel:", "guide" in tel)

print("'jack' not in tel:", "jack" not in tel)

"""
The dict() constructor builds dictionarues directly from sequences of key-value expressions:
"""

tel = dict([("sape", 4139), ("guide", 4127), ("jack", 4098)])
print("tel:", tel)

"""
In addtional, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
"""

print({x: x**2 for x in (2, 4, 6)})

"""
When the keys are simple strings, it is sometimes easire to specify pairs using keyword arguments
"""

print(dict(sape = 4139, guido = 4127, jack = 4098))

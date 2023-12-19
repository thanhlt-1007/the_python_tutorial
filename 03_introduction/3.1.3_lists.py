### 3.1.2. Lists

# Reference: https://docs.python.org/3/tutorial/introduction.html#lists

"""
Python knows a number of compound data types,
used to group together other values.
The most versatile is the list,
which can be written as a list of comma-seperated values (items) between square brackets.
List might contains items of different types, but usually the items all have the same type.
"""

squares = [1, 4, 9, 16, 25]
print("squares:", squares)

"""
Like strings (and all other built-in sequence types), lits can be indexed and sliced
"""

# indexing returns the item
print("squares[0]:", squares[0])

print("squares[-1]:", squares[-1])

# slicing returns a new list
print("squares[-3:]:", squares[-3:])

"""
All slice operations return a new list containing,
the requested elements.
This means that the following slice returns a shallow copy of the list:
"""

print("squares[:]:", squares[:])

"""
Lists also support operations like concatenation:
"""

print("squares + [36, 49, 64, 81, 100]:", squares + [36, 49, 64, 81, 100])

"""
Unlike strings, which are immutable,
lists are a mutable type,
i.e: it is possible to change their content:
"""

# something's wrong here
cubes = [1, 8, 27, 65, 125]
print("cubes:", cubes)

print("4 ** 3 =", 4 ** 3)

# replace the wrong value
cubes[3] = 64
print("cubes:", cubes)

"""
You can also add new items at the end of the list,
by using the list.append() method
"""

# add the cube of 6
cubes.append(216)

# add the cube of 7
cubes.append(7 ** 3)

print("cubes:", cubes)

"""
Assignment to slices is also possible,
and this can even change the size of the list or clear it entirely:
"""

letters = ["a", "b", "c", "d", "e", "f", "g"]
print("letters:", letters)

# replace some values
letters[2:5] = ["C", "D", "E"]
print("letters:", letters)

# now remove them
letters[2:5] = []
print("letters:", letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print("letters:", letters)

"""
The built-in funtion len() also applies
"""

letters = ["a", "b", "c", "d"]
print("letters:", letters)
print("len(letters):", len(letters))

"""
It is possible to nest lists (create lists containing other lists),
for example:
"""

a = ["a", "b", "c"]
print("a:", a)

n = [1, 2, 3]
print("n:", n)

x = [a, n]
print("x:", x)
print("x[0]:", x[0])
print("x[0][1]:", x[0][1])

## 5.3 The tuples and Sequences

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#tuples-and-sequences

"""
We saw that lists and strings have many common properties, such as indexing and slicing operations.
They are two examples of sequence data types (see Sequence Types - list, tuple, range).
Since Python is an evolving language, other sequence data types  may be added.
There is also another standard sequence data type: the tuple.

A tuple consysts of a number of values seperated by commas, for instance:
"""

t = (12345, 54321, 'hello')
print("t:", t)
print("t[0]:", t[0])

"""
Tuples may be nested
"""
u = (t, (1, 2, 3, 4, 5))
print("u:", u)

"""
Tuples are immutable
"""
try:
  t[0] = 888888
except Exception as exception:
  print("exception:", exception)

"""
but they can contain multiple pbjects
"""
v = ([1, 2, 3], [3, 2, 4])
print("v:", v)

"""
As you can see, on output tuples are always enclosed in parenthese, so that nested tuples are interpreted correctly;
they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is pare of a large expression).
It is not possible to assign the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

Though tuples may seem similar to lists, they are often used in different situations and different purposes.
Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via un-packing (see later in this section)
or indexing (or even by attribute in the case of namedtuples).
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these.
Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is con-structed by following a value with a comma
(it is not sufficient to enclose a single parentheses).
Ugly, but effective. For example:
"""

empty = ()
print("empty:", empty)
print("len(empty):", len(empty))

signleton = 'hello',
print("signleton:", signleton)
print("len(signleton):", len(signleton))

"""
The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple.
The reverse operation is alose possible:
"""

x, y, z = t
print("t:", t)
print("x:", x)
print("y:", y)
print("z:", z)

"""
This is called, appropriately enough, sequence unpacking and words for any sequence on the right-hand side.
Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence.
Note that multiple assignment is really just a combination of tuple packing and sequence packing.
"""

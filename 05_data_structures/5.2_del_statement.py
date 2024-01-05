## 5.2 The del statement

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#the-del-statement

"""
There is a way to remove an item from a list given its index instead of its value: the del statement.
This differs from the pop() method which returns a value.
The del statement can also be used to remove slices from a list or clear the entire list
(which we did earlier by assignment of an empty list to the slice).
For example:
"""

a = [-1, 1, 66.25, 333, 333, 1234.5]
print("a:", a)

del a[0]
print("a:", a)

del a[2:4]
print("a:", a)

del a[:]
print("a:", a)

"""
del can also be used to delete entire variables
"""

del a

"""
Referencing the name a hereafter is an error (at least until another value is assigned to it).
We'll find other ises for del later.
"""

try:
  a
except Exception as exception:
  print("exception:", exception)

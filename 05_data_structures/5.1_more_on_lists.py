# 5. Data Structures

"""
This chapter describes somethings you've learned about already in more detail, and adds some new things as well.
"""

## 5.1. More on Lists

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#more-on-lists

"""
The list data type has sime more methods.
Here are all of the methods of list objects:

- list.append(x)

- list.extend(iterable)

- list.insert(i, x)

- list.remove(x)

- list.pop([i])

- list.clear()

- list.index(x[, start[, end]])

- list.count(x)

- list.sort(*. key = None, reverse = False)

- list.reverse()

- list.copy()

An example that uses most of the list methods:
"""

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print("fruits:", fruits)

print("fruits.count('apple'):", fruits.count("apple")) # 2
print("fruits.count('tangerine'):", fruits.count("tangerine")) # 0

print("fruits.index('banana'):", fruits.index("banana")) # 3
print("fruits.index('banana', 4):", fruits.index("banana", 4)) # Find next banana starting at position 4

fruits.sort()
print("fruits:", fruits)

print("fruits.pop():", fruits.pop())
print("fruits:", fruits)

"""
You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed - they return the default None.
This is a design principle for all mutable data structures in Python.

Another thing you might notice is that not all data can be sorted or compared.
For instamce, [None, "hello", 10] doesn't sort because integers can't be compared to strings and None can't be compared to other types.
Also, there are some types that don't have a defined ordering relation. For example, 3+4j < 5+7j isn't a valid comparison.
"""

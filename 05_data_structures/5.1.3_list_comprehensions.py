from math import pi

### 5.1.3. List Comprehension

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#list-comprehensions

"""
List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable,
or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
"""

squares_1 = []
for x in range(10):
  squares_1.append(x**2)
print("squares_1:", squares_1)

"""
Note that this creates (or overwhites) a variable named x that still exists after the loop completes.
We can calculate the list of squares any side effects using:
"""

squares_2 = list(map(lambda x: x**2, range(10)))
print("squares_2:", squares_2)

"""
or, equivalently:
"""

squares_3 = [x**2 for x in range(10)]
print("squares_3:", squares_3)

"""
which is more concise abd readable.

A list comprehension consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for an if clauses which follow it.
For example, this listcomp combines the elements of two lists if they are not equal:
"""

combs_1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("combs_1:", combs_1)

"""
and it's equivalent to:
"""

combs_2 = []
for x in [1, 2, 3]:
  for y in [3, 1, 4]:
    if x != y:
      combs_2.append((x, y))
print("combs_2:", combs_1)

"""
Note how the order of the for and if statements is the same in both these snippets.

If the expressions is a tuple (e.g. the (x, y)) in the previous example), it must be parenthesized.
"""

vec = [-4, -2, 0, 2, 4]
print("vec:", vec)

# create a new list with the values doubled
doubleds = [x*2 for x in vec]
print("doubleds:", doubleds)

# filter the list to exclude negative numbers
non_negative_numbers = [x for x in vec if x >= 0]
print("non_negative_numbers:", non_negative_numbers)

# apply a function to all the elements
abses = [abs(x) for x in vec]
print("abses:", abses)

fresh_fruits = ["   banana", "  loganberry  ", "passion fruit  "]
print("fresh_fruits:", fresh_fruits)

# call a method on each element
strips = [weapon.strip() for weapon in fresh_fruits]
print("strips:", strips)

# create a list of 2-tuples like (number, square)
tuples = [(x, x **2) for x in range(6)]
print("tuples:", tuples)

# the tuple must be parenthesized, otherwise an error is raised
# try:
#   [x, x**2 for x in range(6)]
# except Exception as exception:
#   print(exception)

list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("list_2d:", list_2d)

flatten_list = [num for list_1d in list_2d for num in list_1d]
print("flatten_list:", flatten_list)

"""
List comprehensions can contain complex expressions and nested functions:
"""

round_pies = [str(round(pi, i)) for i in range(1,  6)]
print("round_pies:", round_pies)

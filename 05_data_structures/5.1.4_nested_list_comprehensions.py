### 5.1.4. Nested List Comprehension

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#nested-list-comprehensions

"""
The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
"""

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
print("matrix:", matrix)

"""
The following list comprehension will transpose rows and columns
"""

transposed_matrix_1 = [[row[i] for row in matrix] for i in range(4)]
print("transposed_matrix_1:", transposed_matrix_1)

"""
As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it,
so this example is equivalent to:
"""

transposed_matrix_2 = []
for i in range(4):
  transposed_matrix_2.append([row[i] for row in matrix])
print("transposed_matrix_2:", transposed_matrix_2)

"""
which, in turn, is the same as:
"""
transposed_matrix_3 = []
for i in range(4):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  transposed_matrix_3.append(transposed_row)
print("transposed_matrix_3:", transposed_matrix_3)

"""
In the real world, you should prefer built-in functions to complex statements.
The zip() function would do a great job for this use case:
"""

print("list(zip(*matrix)):", list(zip(*matrix)))

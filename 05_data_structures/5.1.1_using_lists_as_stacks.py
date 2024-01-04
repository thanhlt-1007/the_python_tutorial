### 5.1.1. Using Lists as Stacks

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#using-lists-as-stacks

"""
The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved ("last-in, first-out").
To add an item to the top of the stack, use append().
To retrieve an item from the top of the stack, use pop() without an explicit index.
For example
"""

stack = [3, 4, 5]
print("stack:", stack)

stack.append(6)
stack.append(7)
print("stack:", stack)

print("stack.pop():", stack.pop())
print("stack:", stack)

print("stack.pop():", stack.pop())
print("stack:", stack)

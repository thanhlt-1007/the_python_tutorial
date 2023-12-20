## 4.3. The range() Function

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#the-range-function

"""
If you do need to iterate over a sequence of numbers,
the built-in gunction range() comes in handy.
It generates a arithmetic progressions:
"""

for i in range(5):
  print(i)

"""
The given end point is never part of the generated sequence;
range(10) generates 10 values,
the legal indices for items of a sequence of length 10.
It is possible to let the range start at another number,
or to specify a different increment (even negative; sometimes this is called the 'step')
"""

print("list(range(5, 10)):", list(range(5, 10)))
print("list(range(0, 10, 3)):", list(range(0, 10, 3)))
print("list(range(-10, -100, -30)):", list(range(-10, -100, -30)))

"""
To iterate over the indices ò a sequence,
you can combine range() and len() á follows:
"""

a = ["Mary", "had", "a", "little", "lamb"]
print("a:", a)

for i in range(len(a)):
  print(i, a[i])

"""
In most such cases, however, it is convenient to use the enumerate() function,
A strange thing happens if you just print a page:
"""

print("range(10):", range(10))

"""
In many ways the object returned by range() behaves as if it is a list,
but in fact it isn't.
It is an object which returns the successive items of the desired sequence when you iterate overit,
but it doesn't really make the list,
thus saving space.
We say such an object is iterate, that is,
suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.
We have seen that the for statement is such a construct, while an example of a function that takes an iterable is sum()
"""

print("sum(range(4)):", sum(range(4)))

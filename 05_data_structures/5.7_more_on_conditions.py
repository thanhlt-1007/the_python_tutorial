## 5.7. Mpre on Conditions

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#more-on-conditions

"""
The conditions used in while and if statements can contain any operators, not just comparisons.

The comparision operators in and not in are membership tests that determine whether a value is in (or not in) a container.
The operator is and is not compare whether two objects are really the same object.
All comparision operators have the same priority, which is lower than that of all numerical operators.

Comparisions can be chained.
For example, a < b == c tests whether a is less than b and moreover b equals c.

Comparisions may be combined using the Boolean operators and and or, and the outcome of a comparision (or of any other Boolean expression) may be negated with not.
These have lower prioritis than comparision operators; between them. not has the highest priority and or the lowest,
so that A and not B or C is equivalent to (A and (not B)) or C.
As always, parenthese can be used to express the desired composition.

The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.
For example, if A and C are true but B is false, A and B and C does not evaluate the expression C.
When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result if a comparision or other Boolean expression to a variable.
For example:
"""

string1, string2, string3 = "", "Trondheim", "Hammer Dance"
non_null = string1 or string2 or string3
print("non_null:", non_null)

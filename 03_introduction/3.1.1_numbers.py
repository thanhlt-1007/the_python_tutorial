import sys
import traceback

# 3. An Informal Introduction to Python

print("3. An Informal Introduction to Python")

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "This is not a comment because it's inside quotes."

## 3.1 Using Python as a Calculator

### 3.1.1. Numbers

# Reference: https://docs.python.org/3/tutorial/introduction.html#numbers

print("3.1.1. Numbers")

"""
The interpreter acts as a simple calculator:
you can type an expression at it and it will write the value.
Expression syntax is straightforward:
the operators
- +
- -
- *
- /
can be used to perform arithmetic;
parentheses () can be used for grouping.
For example:
"""

print("2 + 2 =", 2 + 2)
print("50 - 5 * 6 =", 50 - 5 * 6)

# division always returns a floating point number
print("(50 - 5 * 6) / 4 =", (50 - 5 * 6) / 4)
print("8 / 5 =", 8 / 5)

"""
The integer numbers (e.g: 2. 4, 20) have type int,
the ones with a fractional part (e.g: 5.0, 1.6) have type float.
We will see more about numeric types later in the tutorial.

Division (/) always return a float.
To do floow division and get an integer result you can use the // operator;
to calculate the remainder you can use %:
"""

# classic division returns a flow
print("17 / 3 =", 17 / 3)

# floor division discards the fractional part
print("17 // 3 =", 17 // 3)

# the % operator returns the remainder of the division
print("17 % 3 =", 17 % 3)

# floored quotient * divisor + remainder
print("5 * 3 + 2 =", 5 * 3 + 2)

"""
With Python, it is possible to use the ** operator to calculate powers
"""

# 5 squared
print("5 ** 2 =", 5 ** 2)

# to the power of 7
print("2 ** 7 =", 2 ** 7)

"""
The equal sign = is used to assign a value to a variable.
Afterwards, no result is displayed before the next interactive prompt:
"""

width = 20
print("width =", width)

height = 5 * 9
print("height =", height)

print("width * height =", width * height)

"""
If a variable is not "defined" (assigned a value),
trying to use it will give you an error

# try to access an undefined variable
n
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined
"""

print("Try to access an undefined variable")
try:
  n
except Exception as exception:
  ex_type, ex_value, ex_traceback = sys.exc_info()
  print("ex_type:", ex_type)
  print("ex_value:", ex_value)
  print("ex_traceback:", ex_traceback)
  print("print_exc")
  traceback.print_exc()
  print("print_exception")
  traceback.print_exception(*sys.exc_info())

"""
There is full support for floating point;
operators with mixed type operands convert the integer operand to floating point:
"""

print("4 * 3.75 - 1 =", 4 * 3.75 - 1)

"""
In interactive mode,
the last printed expression is assigned to the variable _.
This means that when you are using Python as a desk calculator,
it is somewhat easier to continue calculations,
for example:
"""

tax = 12.5 / 100
print("tax =", tax)

price = 100.50
print("price =", price)

print("price * tax =", price * tax)

"""
In addtion to int and float,
Python supports other types of numbers,
such as Decimal and Fraction.
Python also has built-in support for complex, numbers,
and use the j or J suffox to indicate the imaginary part (e.g: 3 + 5j)
"""

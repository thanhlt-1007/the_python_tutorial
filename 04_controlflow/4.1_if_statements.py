# 4. More Control Flow Tools

## 4.1. if Statements

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#if-statements

"""
Perhaps the most well-known statement tyoe is the if statement.
For example:
"""

x = int(input("Please enter an integer: "))
if x < 0:
  x = 0
  print("Negative changed ro zero")
elif x == 0:
  print("Zero")
elif x == 1:
  print("Single")
else:
  print("More")

"""
There can be zero or more elif parts,
and the elif part is optional.
The keyword elif is short for else if,
and is useful for avoid excessive indentation.
And
  if ...
  elif ...
  elif ...
sequence is a substitute for the switch or case statements found in the other languages.
If you're comparing the same value to several constants,
or checking for specific types or attributes,
you may also find the match statement useful.
For more details see match Statements.
"""

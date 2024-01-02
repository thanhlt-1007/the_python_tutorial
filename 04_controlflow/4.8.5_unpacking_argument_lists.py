### 4.8.5. Unpacking Argument Lists

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#unpacking-argument-lists

"""
The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring seperate positional arguments.
For instance, the built-in range() function expects seperate start and stop arguments.
If they are not available separately, write the function call with the * operator to unpack the arguments out of a list or tuple:
"""

print("list(range(3, 6)):", list(range(3, 6)))

args = [3, 6]
print("args:", args)

print("list(range(*args)):", list(range(*args)))

"""
In the same fashion, dictionaries can be deliver keyword arguments with the ** operator
"""

def parrot(voltage, state = "a stiff", action = "voom"):
  print("-- This parrot wouldn't", action, end = " ")
  print("if you put", voltage, "volts through it.", end = "")
  print("E's", state, "!")

d = { "voltage": "four million", "state": "bleedin' demised", "action": "VOOM" }
parrot(**d)

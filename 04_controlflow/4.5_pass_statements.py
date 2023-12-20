## 4.5. pass Statements

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#pass-statements

"""
The pass statement does nothing.
It can be used when a statement is required syntactically but the program requires no action.
For example:
"""

# while True:
#   print("Busy-wait for keyboard interrupt (Ctrl + C) ...")
#   pass

"""
This is commonly used for creating minimal classes:
"""

class MyEmptyClass:
  pass

"""
Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code,
allowing you to keep thinking at a more abstract level.
The pass is silently ignored:
"""

def initlog(*args):
  # Remember to implement this!
  pass

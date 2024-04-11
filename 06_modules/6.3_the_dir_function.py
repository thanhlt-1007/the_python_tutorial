# 6.3 The dir() function

# Reference: https://docs.python.org/3.12/tutorial/modules.html#the-dir-function

"""
The built-in function dir is used to find out which names a module defines.
It returns a sorted list of strings:

Without arguments, dir() lists the names you have defined currently
"""

import fibo

a = [1, 2, 3, 4, 5]
fib =fibo.fib
print(dir())

"""
Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables.
If you want a list of those, they are defined in the standard module builtins:
"""

import builtins

print(dir(builtins))

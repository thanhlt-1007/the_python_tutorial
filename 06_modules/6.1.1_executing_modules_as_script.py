# 6.1.1 Executing modules as scripts

# Reference: https://docs.python.org/3.12/tutorial/modules.html#executing-modules-as-scripts

"""
When you run a Python module with

python fibo.py <arguments>

the code in the module will be executed, just as if you imported, but with the __name__ set to "__main__".
That means that by adding this code at the end of your module:
"""

# if __name__ == "__main__":
#   import sys
#   fib(int(sys.argv[1]))

"""
you can make the file isable as a script as well as an importable module,
because the code that parses the command like only runs if the module is executed as the "main" file:
"""

# python fipo.py 50

"""
If the module is imported, the code is not run:
"""

# import fibo

"""
This is often used either to provide a conveninent user interface to a module, or for testing purposes (running the module as a script executes a test suite).
"""

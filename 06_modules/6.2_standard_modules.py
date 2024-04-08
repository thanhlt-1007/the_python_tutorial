# 6.2 Standard Modules

# Reference: https://docs.python.org/3.12/tutorial/modules.html#standard-modules

"""
Python comes with a library of standard modules, described in a seperate document, the Python Library Reference ("Library Reference" hereafter).
Some modules are built in the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built in, either for effeciency or to provide access to operation system primitives such as system calls.
The set of such modules is a configuration option which also depends on the underlying platform.
For example, whe winreg module is only provided on Window systems.
One particular module deserves some attention: sys, which is build into every Python interpreter.
The variable sys.ps1 and sys.ps2 define the strongs used as primary and secondary prompts:
"""

# import sys
# sys.ps1
# sys.ps2

"""
These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings the determines the interpreter's search path for modules.
It is initialized to a default path taken from the environment variable PYTHONPATH, or from a built-in default if PYTHONPATH is not set.
You can modify it using standard list operations:
"""

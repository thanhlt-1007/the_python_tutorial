# 6.1.3 "Compiled" Python files

# Reference: https://docs.python.org/3.12/tutorial/modules.html#compiled-python-files

"""
To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file; it general contains the Python version number.
For example, in CPython relerase 3.3 the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc.
This naming convention allows compiled modules from different releases and different versions of Python to coexists.

Python checks the modification date of the source against the compiled version to see if it's out of date and needs to be recompiled.
This is a completely automatic process.
Also, the compiled modules are platform-indepedent, so the same library can be shared among systems with different architectures.

Python does not check the cache in two circumstances.
First, it always recompiles and does not store the result for the module that's loaded directly from the command line.
Second, it does not check the cache if there is no source code.
To support a non-source (compiled only) distribution, the compiled module must be in the source firectory, and there must not be a source module.

Some tips for experts:

- You can use the -0 or -00 switches on the Python command to reduce the size of a compiled module.
The -0 switch removes assert statements, the -00 switch removes both assert statements and __doc__ strings.
Since some programs may reply on having these available, you should only use this option if you know what you're doing.
"Optimized" modules have an opt- tag and are usually smaller.
Future releases may change the effects of optimization.

- A program doesn't run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that's faster about .pyc files is the speed with which they are loaded.

- The module compileall can create a .pyc files for all modules in a directory.

- There is more detail on this process, including a flow chart of the decision.
"""

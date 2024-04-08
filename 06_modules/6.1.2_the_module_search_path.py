# 6.1.2 The module search path

# Reference: https://docs.python.org/3.12/tutorial/modules.html#the-module-search-path

"""
When a module named spam is imported, the interpreter first searches for a built-in module with that name.
These module names are listed in sys.builltin_module_names.
It not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.
sys.path is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).
- PYTHONPATH (a list of directory names, whith the same syntax as the shell variable PATH).
- The installation-dependent default (by convention including a site-packages directory, handled by the site module)

More detauks are at The initialization of the sys.path module search path.

Note: On file system which support symlinks, the directory containing the input script is calculated after rge symlink is followed.
In other words the directory containing the symlink is not added to the module search path.

After initialization, Python programs can modify sys.path.
The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path.
This means that scripts in that directory will be loaded instead of modules of the same name in the library directory.
This is an error unless the replacement intended.
See action Standard Modules for more information.
"""

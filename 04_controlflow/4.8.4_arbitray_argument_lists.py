### 4.8.4. Arbitrary Argument Lists

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#arbitrary-argument-lists

"""
Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments.
These arguments will be wrapped up in a tuple (see Tuple and Sequences).
Before the variable number of arguments, zero or more normal argument may occur.
"""

def write_multiple_items(file, separator, *args):
  file.wrire(separator.join(args))

"""
Normally, these variadic arguments will be last in the list of formal parameters,
because thet scoop up all remaining input arguments that are passed in to the function.
Any formal parameters which occur after the *args parameter are keyword-only arguments,
meaning that they can only be used as keywords rather than positional arguments.
"""

def concat(*args, sep = "/"):
  return sep.join(args)

print('concat("earth", "mars", "venus"):', concat("earth", "mars", "venus"))
print('concat("earth", "mars", "venus", sep = "."):', concat("earth", "mars", "venus", sep = "."))

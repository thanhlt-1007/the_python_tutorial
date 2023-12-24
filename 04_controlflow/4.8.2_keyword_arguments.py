### 4.8.2. Keyword Arguments

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#default-argument-values

"""
Functions can also be called using keyword arguments of the form kwargs=value.
For instance, the following function:
"""

def parrot(voltage, state = "a stiff", action = "voom", type = "Norwegian Blue") -> None:
  print("-- This parrot wouldn't", action, end = " ")
  print("if you put", voltage, "volts through it.")
  print("-- Lovely plumage the", type)
  print("-- It's", state, "!")

"""
accepts one required argument (voltage)
and three optional arguments (state, action and type).
This function can be called in any of the following ways:
"""

# 1 positional argument
parrot(1000)

# 1 keyword argument
parrot(voltage = 1000)

# 2 keywords arguments
parrot(voltage = 1000, action = "VOOOOOM")

# 2 keywords arguments
parrot(action = "VOOOOOM", voltage = 1000)

# 3 positional arguments
parrot("a million", "bereft of life", "jump")

# 1 positional, 1 keyword
parrot("a thousand", state = "pushing up the daisies")

"""
but all the following calls would be invalid
"""

# required argument missing
try:
  parrot()
except Exception as exception:
  print(exception)

# non-keyword argument after a keyword argument
# try:
#   parrot(voltage = 5.0, "dead")
# except Exception as exception:
#   print(exception)

# duplicate value for the same argument
try:
  parrot(110, voltage = 220)
except Exception as exception:
  print(exception)

# unknown keyword argument
try:
  parrot(actor = "John Cleese")
except Exception as exception:
  print(exception)

"""
In a function call, keyword arguments must follow positional arguments.
All the keyword arguments passed must match one of the argument accepted by the function
(e.g. actor is not a valid argument for the parrot function),
and their order is not important.
This also include non-optional arguments (e.g. parrot(voltage = 1000) is valid too).
No argument may receive a value more than once.
Here's an example that fails due to this restriction:
"""

def empty_function(a) -> None:
  pass

try:
  empty_function(0, a = 0)
except Exception as exception:
  print(exception)

"""
When a final formal parameter of the form **name is present,
it receives a dictionary (see Mapping Types - dict) containing all keyword arguments except for those corresponding to a formal parameter.
This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a typle containing the positional arguments beyond the formal parameter list.
(*name must occur before **name.)
For example, if we define a function like this:
"""

def cheese_shop(kind, *arguments, **keywords) -> None:
  print("-- Do you have any", kind, "?")
  print("-- I'm sorry, we're all of out", kind)
  for arg in arguments:
    print(arg)
  print("-" * 40)
  for kw in keywords:
    print(kw, ":", keywords[kw])

cheese_shop("Limburger",
            "It's very runny, sir",
            "It's really very, VERY runy, sir",
            shop_keeper = "Micheal Palin",
            client = "John Cleese",
            sketch = "Cheese Shop Sketch")

"""
Note that the order in which the keyword arguments are printed is guaranteed to match the order in which they were provided in the function call.
"""

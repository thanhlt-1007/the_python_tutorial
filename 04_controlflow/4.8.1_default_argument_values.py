### 4.8.1. Default Argument Values

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#default-argument-values

"""
The most useful form is to specify a default value for one or more arguments.
This creates a function that can be called with fewer arguments than it is defined to allow.
For example
"""

def ask_ok(prompt, retries = 4, reminder = "Please try again!") -> bool:
  while True:
    reply = input(prompt)
    if reply in { "y", "ye", "yes" }:
      return True
    if reply in { "n", "no", "nop", "nope" }:
      return False

    retries = retries - 1
    if retries < 0:
      raise ValueError("Invalid user response")

    print(reminder)

"""
This function can be called in several ways:

- giving only the mandatory argument:
"""

ask_ok("Do you really want to quit? ")

"""
- giving one of the optional arguments:
"""

ask_ok("OK to overwrite the file? ", 2)

"""
or even giving all arguments:
"""

ask_ok("OK to overwrite the file? ", 2, "Come on, only yes or no!")

"""
This example also introduces the in keyword.
This tests whether or not a sequence contains a certain value.

The default values are evaluated at the point of function definition in the defining scope, so that
"""

i = 5

def print_i_value(i_value = i) -> None:
  print(i_value)

i = 6
print_i_value() # 5

"""
Important warning: The default value is evaluated only once.
This makes a different when the default is a mutable object such as a list, dictionary, or instance of most classes.
For example, the following function accumulates the arguments passed to it on subsequent calls:
"""

def append_L(value, L = []) -> list:
  L.append(value)
  return L

print(append_L(1)) # [1]
print(append_L(2)) # [1, 2]
print(append_L(3)) # [1, 2, 3]

"""
If you don't want the default to be shared between subsequent calls,
you can write the function like
"""

def re_init_and_append_L(value, L = None) -> list:
  if L is None:
    L = []

  L.append(value)
  return L

print(re_init_and_append_L(1)) # [1]
print(re_init_and_append_L(2)) # [2]
print(re_init_and_append_L(3)) # [3]

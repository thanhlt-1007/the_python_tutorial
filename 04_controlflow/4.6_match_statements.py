from enum import Enum

## 4.6. match Statements

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#match-statements

"""
A match statement takes an expression and compare its value to successive patterns give as one or more case blocks.
This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages),
but it's more similar to pattern matching in languages like Rust or haskell.
Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

The simplest form compares a subject value against one or more literals:
"""

def http_error(status) -> str:
  match status:
    case 400:
      return "Bad Request"
    case 401 | 403 | 404:
      return "Not allowed"
    case 404:
      return "Not found"
    case 418:
      return "I'm a teapot"
    case _:
      return "Something's wrong with the internet"

print(http_error(400))

"""
Note the last block: the variable name _ acts a wildcard and never fails to match.
If no case matches, none of the branches is executed.

You can combine several literals in a single pattern using | ("or"):

case 401 | 403 | 404:
  return "Not allowed"

Patterns can look like unpacking assignments,
and can be used to bind variables:
"""

# point is an (x, y) tuple
point = (0, 1)
match point:
  case (0, 0):
    print("Origin")
  case (0, y):
    print(f"Y={y}")
  case (x, 0):
    print(f"X={x}")
  case (x, y):
    print(f"X={x}, Y={y}")
  case _:
    raise ValueError("Not a point")

"""
Study that one carefully!
The first pattern has two literals,
and can be though of as an extension of the literal pattern shown above.
But the next two patterns combine a literal and a variable,
and the variablle binds a value from the subject (point).
The fourth pattern captures two variables,
which makes it conceptually similar to the unpacking assignment (x, y) = point.

If you are using classes to structure your data you can use the class name followed by an argument list resembling a constructor,
but with the ability to capture attributes into variables:
"""

class Point:
  def __init_(self, x, y):
    self.x = x
    self.y = y

def where_is(point) -> None:
  match point:
    case Point(x = 0, y = 0):
      print("Origin")
    case Point(x = 0, y = y):
      print(f"Y={y}")
    case Point(x = x, y = 0):
      print(f"X={x}")
    case Point():
      print("Somewhere else")
    case _:
      print("Not a point")

"""
You can use positional parameters with some builtin classes that provide an ordering for their attributes (e.g. dataclasses).
You can also define a specific position for attributes in patterns by setting the __match_args__ special attribute in your classes.
If it's set to ("x", "y"),
the following patterns are all equivalent (and all bind the y attribute to the var attribute):

Point(1, var)
Point(1, y = var)
Point(x = 1, y = var)
Point(y = var, x = 1)

A recommended way to read patterns is to look at them as an extended from of what you would put on the left of an assignment,
to understand which variables would be set to what.
Only the standalone names (like var above) are assigned to by a match statement.
Dotted names (like foo.bar), attribute names (the x= and y= above) or class names (recognized by the "(...)") next to them like Point above) and never assigned to.

Patterns can be arbitrarily nested.
For example, if we have a short list of Points, with ___match_args__ added, we could match it like this:
"""

class Point:
  __match_args__ = ("x", "y")
  def __init__(self, x, y):
    self.x = x
    self.y = y

points = []
match points:
  case []:
    print("No points")
  case [Point(0, 0)]:
    print("The origin")
  case [Point(x, y)]:
    print(f"Single point {x}, {y}")
  case [Point(0, y1), Point(0, y2)]:
    print(f"Two on the Y axis at {y1} {y2}")
  case _:
    print("Something else")

"""
You can add an if clause to a pattern, known as a guard.
If the guard is false, match goes on to try the next case block.
Note that value capture happens before the guard is evaluated:
"""

match point:
  case Point(x, y) if x == y:
    print(f"Y=X at {x}")
  case Point(x, y):
    print(f"Not on the diagonal")

"""
Several other key features of this statement:

- Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequence.
An important exception is that they don't match iterators and strings.

- Sequence patterns support extended unpacking: [x, y, *rest] and (x, y, *rest) work similar to unpacking assignments.
The name after * may also be _, so (x, y, *_) matches a sequence of at least two items without binding the remaining items.

- Mapping patterns {"bandwidth": b, "latency": l} captures the "bandwidth" and "latency" values from a dictionary.
Unlike sequence patterns, extra keys are ignored.
An unpacking like **rest is also supported.
But **_ would be redundant, so it is now allowed.

- Suppatterns may be captured using as keyword:
case (Point(x1, y1), Point(x2, y2) as p2): ...
will capture the second element of the input as p2 (as long as the input is a sequence of two points)

- Most literals are compared by equality, however the singletons True, False and None are compared by identity.

- Patterns may use named constants.
These must be dotted names to prevent them from being interpreted as capture variable:
"""

class Color(Enum):
  RED = "red"
  GREEN = "green"
  BLUE = "blue"

color = Color(input("Enter your choice of 'red', 'green' or 'blue': "))

match color:
  case Color.RED:
    print("I see red!")
  case Color.GREEN:
    print("Grass is green")
  case Color.BLUE:
    print("I'm feeling the blue :(")

"""
For a more detailed explanation and addtional examples,
you can look into PEP 636 which is written in a tutorial format.
"""

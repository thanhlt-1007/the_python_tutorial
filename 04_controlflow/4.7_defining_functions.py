## 4.7. Defining Functions

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#defining-functions

"""
We can create a function that writes the Fibonacci series to an arbitrary boundary:
"""

# write Fibonacci series up to n
def fib(n) -> None:
  """
  Print a Fibonacci series up to n.
  """
  a, b = 0, 1
  while a < n:
    print(a, end = " ")
    a, b = b, a + b
  print()

# Now call the function we just defined:
fib(2000)

"""
The keyword def introduces a function definition.
It must be followed by the function name and the parenthesized list of formal parameters.
The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal;
this string literal is the function's documentation string, or docstring.
(More about docstring can be found in the section Documentation Strings.)
There are tools which use docstrings to automatically produce online or printed documentation,
or to let the user interactively browse through code;
it's good practice to include docstrings in code that you write, so make a habit of it.

The execution of a function introduces a new symbol table used for the local variables of the function.
More precisely, all variables assignment in a function store the value in the local symbol table:
whereas variable references first look in the local symbol table,
then in the local symbol tables of enclosing functions,
then in the global symbol table, and finally in the table of built-in names.
Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function
(unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement),
although they may be referenced.

The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called;
thus, argument are passed using call by value (where the value is always an object reference, not the value of the object).
When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.

A function definition associates the function name with the function object in the current symbol table.
The interpreter reconizes the object pointed to be that name as a user-defined function.
Other names can also point to that same function object and can also be used to access the function:
"""

print("fib:", fib)

f = fib
f(100)

"""
Coming from other languages, you might object that fib is not a function but a procedure since it doesn't return a value.
In fact, even functions without a return statement do a return value, albet a rather boring one.
This value is called None (it's a built-in name).
Writing the value None is normally suppressed by the interpreter if it would be the only value written.
You can see it if you really want to using print()
"""

fib(0)
print(fib(0)) # None

"""
It is simple to write a function that returns a list of the number of the Fibonacci series,
instead of printint it:
"""

# return Fibonacci series up to n
def fib2(n) -> list:
  """
  Return a list containing the Fibanacci series up to n.
  """
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, b + a
  return result

f100 = fib2(100)
print("f100:", f100)

"""
This example, as usual, demonstrates some new Python features:

- The return statement returns with a value from a function.
return without an expression argument returns None.
Falling of the end of a function also return None.

- The statement result.append(a) calls a method of the list object result.
A method is a function that belongs to an object and is named obj.methodname,
where obj is some object (this may be an expression),
and methodname is the name of a method that is defined by the object's type.
Different types define different methods.
Methods of different types may have the same name without causing ambiguity.
(It is possible to define your own object types and methods, using classes, see Classes).
The method append() shown in the example is defined for list object;
it adds a new element at the end of the list.
In this example it is equivalent to result = result + [a], but more efficient.
"""

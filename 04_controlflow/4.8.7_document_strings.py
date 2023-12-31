### 4.8.7. Documentation Strings

# Reference: https://docs.python.org/3.12/tutorial/controlflow.html#documentation-strings

"""
Here are some conventions about the content and formatting of documentation strings.

The first line should always be a short, concise summary of the object's purpose.
For brevity, it should not explicitly state that object's name or type, since these are available by other means
(except if the name happens to be a verb describing a function's operation).
This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string,
the second line should be blank,
visually seperating the summary from the rest of the description.
The following lines should be one or more paragraphs describing the object's calling conventions, its side effects, etc.

The Python parser does not strip indentation from multi-line string literals in Python,
so tools that process documentation have to strip indentation is desired.
This is done using the following concention.
This first non-blank line after the first line of the string determines the amount of indentation for the entire documentation string.
(We can't use the first line since it is generally adjacent to the  string's opening quotes so its indentation is not apparent in the string literal.)
Whitespace "equivalent" to this indentation is then stripped from the start of all lines of the string.
Lines that are indented less should not occur, but if they occur all their leading whitespace should be stripped.
Equivalence of whitespace should be tested after expansion of tabs.

Here is an example of a multi-line docstring:
"""

def my_function():
  """
  Do nothing, but document it.

  No, really, it doesn't anythong.
  """
  pass

print(my_function.__doc__)

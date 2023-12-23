# Reference: https://docs.python.org/3.12/tutorial/interpreter.html

# 2. Using the Python Interpreter

## 2.1. Invoking the Interpreter

### 2.1.1. Argument Passing

### 2.1.2. Interactive Mode

print("2.1.2. Interactive Mode")

the_world_is_flat = True
if the_world_is_flat:
  print("Be careful not to fall off!")

## 2.2. The Interpreter and Its Environment

# 2.2.1. Source Code Encoding

"""
By default, Python source files are treated as encoded in UTF-8.
In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments - although the standard library only uses ASCII characters for identifiers,
a convention that any portable code should follow.
To display all these characters properly,
your editor must recognize that the file is UTF-8,
and it must use a font that supports all the characters in the file.

To declare an encoding other than the default one,
a special comment line should be added as the first line of the file.
The syntax is as follows:

# -*- coding: encoding -*-

Where encoding is one of the valid codes supported by the Python.

For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

# -*- coding: cp1252 -*-

One exception to the first line rule is when the source code starts with a UNIX "shebang" line.
In this case, the encoding declaration should be added as the second line of the file.
For example:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""

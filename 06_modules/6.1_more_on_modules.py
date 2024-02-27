# 6.1 More on Modules

# Reference: https://docs.python.org/3.12/tutorial/modules.html#more-on-modules

"""
A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module.
They areexecuted onlythe first time the module name is encountered in an import statement.
(They are also run if the file is executed as a script.)

Each module has its own private namespaces, which is used as the global namespace bt all functions defined in the module.
This, the author of a module can use global variables in the module without worrying about accidental clashes with a user's global variables.
On the other hand, if you know what you are doing you can touch a module's global variables with the same notation used to refer to its functions, modname.itemname.

Modules can import other modules.
It is customary but not required to place all import statements at the beginning of a module (or script, for that matter).
The imported module names, if placed at the top of a module (outside any functions ar classes), are added to the module's global namespace.

There is a variant of the import statement that imports names from a module directly into the importing module's namespace.
For example:
"""

from fibo import fib, fib2
fib(500)

"""
This does not introduce the module name from which the imports are taken in the local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:
"""

from fibo import *
fib(500)

"""
This imports all names except those beginning with an underscore (_).
In most cases Python programmers do not use this facility since it introduces an unknow set os names into the interpreter, possibly somethings you have already defined.

Not that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code.
However, it is okay to use it to save typing in tnteractive sessions.

If the module name is followed by as, then the name following as is bound directly to the imported module.
"""

import fibo as fib
fib.fib(500)

"""
This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib.

It can also be used when utlising from with similar effects:
"""

from fibo import fib as fibonacci
fibonacci(500)

"""
Note: For efficiency reasons, each modules is only imported once per interperte session.
Therefore, if you change your modules, you must restart the interpreter - or, if it's just one module you want to test interactively,
use importlib.reload(), eg:
import importlib;
importlib.reload(modulename)
"""

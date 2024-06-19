
![test-driven-development-process-cycle-xenonstack](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/d5929a86-fc9e-4b3f-8772-152b74c7d3b0)

**Completion:** 100%

**Title:** Python - Test-driven development

**Level:** Amateur

**By:** Guillaume

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

## Background Context

Important notice on intranet checks for Python projects Starting from today:

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
- Don’t trust the user, always think about all possible edge cases

## Resources

Read or watch:

- [doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html#what-is-doctest)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

## Quiz questions

Great! You've completed the quiz successfully! Keep going! (Hide quiz)

Question #0

Is this a standardized way to comment a function in Python?

/* Addition function */

def add(a, b):

    return a + b

- Yes

- No

Question #1

Is this a standardized way to comment a function in Python?

"""" Addition function """

def add(a, b):

    return a + b

- Yes

- No

Question #2

Is this a standardized way to comment a function in Python?

##########

# Addition function

##########

def add(a, b):

    return a + b

- Yes

- No

Question #3

Is this a standardized way to comment a function in Python?

def add(a, b):

    """ Addition function """

    return a + b

- Yes

- No

Question #4

Is this module correctly commented?

#!/usr/bin/python3

""" 

My calculation module

"""

import sys

...

- Yes

- No

Tips:

Docstring must be before import statements

Question #5

Is this module correctly commented?

#!/usr/bin/python3

import sys

""" 

My calculation module

"""

...

- Yes

- No

Tips:

Docstring must be before import statements

Question #6

Based on this code, what should all the test cases be? (select multiple)

def uniq(list):

    """ Returns unique values of a list """

    u_list = []

    for item in list:

        if item not in u_list:

            u_list.append(item)

    return u_list

- empty list

- list with one element (any type)

- list with 2 different element (same type)

- list with twice the same element (same type)

- list with more than 2 times the same element (same type)

- list with multiple types (integer, string, etc…)

- not a list argument (ex: passing a dictionary to the method)

| Filename                        | Description                                                                                      |
|---------------------------------|--------------------------------------------------------------------------------------------------|
| 0-add_integer.py                | Function `add_integer(a, b=98)` adds two integers. Inputs must be integers or floats.            |
| 2-matrix_divided.py             | Function `matrix_divided(matrix, div)` divides all elements of a matrix by a divisor.            |
| 3-say_my_name.py                | Function `say_my_name(first_name, last_name="")` prints a formatted name string.                  |
| 4-print_square.py               | Function `print_square(size)` prints a square of '#' characters of given size.                   |
| 5-text_indentation.py           | Function `text_indentation(text)` prints text with new lines after '.', '?', and ':' characters. |
| 6-max_integer.py                | Function `max_integer(list)` finds the maximum integer in a list.                                |
| tests/6-max_integer_test.py     | Unittests for `max_integer` function covering various cases including edge cases.                |
| 100-matrix_mul.py               | Function `matrix_mul(m_a, m_b)` multiplies two matrices.                                          |
| 101-lazy_matrix_mul.py          | Function `lazy_matrix_mul(m_a, m_b)` performs matrix multiplication using NumPy.                 |
| tests/101-lazy_matrix_mul.txt   | Tests for `lazy_matrix_mul` function covering various cases including error handling.           |

AUTHOR : BAPTISTE POUQUEROU

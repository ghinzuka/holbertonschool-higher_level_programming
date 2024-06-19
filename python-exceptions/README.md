# Python - Exceptions

![Project Badge](badge-url)

**Completion:** 100%

**Title:** Python - Exceptions

**Level:** Amateur

**By:** Guillaume

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

## Background Context

This project focuses on understanding and implementing exception handling in Python. You'll explore the differences between errors and exceptions, learn how to handle exceptions effectively, and practice raising built-in exceptions.

## Resources

Read or watch:

- [Errors and Exceptions](https://example.com)
- [Learn to Program 11 Static & Exception Handling](https://example.com) (starting at minute 7)

The above resources provide comprehensive coverage on error handling and exceptions in Python. It's recommended to go through these materials to grasp the concepts thoroughly.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a built-in exception
- When do we need to implement a clean-up action after an exception

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

More Info
Documentation is now mandatory! Each module, class, and method must contain docstring as comments. Example Google Style Python Docstrings

## tasks

| Filename                        | Description                                                                                          |
|---------------------------------|------------------------------------------------------------------------------------------------------|
| 0-safe_print_list.py             | Function `safe_print_list` prints x elements of a list `my_list`, handling any type of elements. Returns number of elements printed. |
| 1-safe_print_integer.py          | Function `safe_print_integer` prints an integer value using "{:d}".format(). Returns True if printed correctly, False otherwise. |
| 2-safe_print_list_integers.py    | Function `safe_print_list_integers` prints first x integers from `my_list`. Skips non-integers. Returns number of integers printed. |
| 3-safe_print_division.py         | Function `safe_print_division` divides two integers a and b, prints the result. Returns result or None if exception occurs. |
| 4-list_division.py               | Function `list_division` divides element by element two lists `my_list_1` and `my_list_2`. Returns new list with division results. |
| 5-raise_exception.py             | Function `raise_exception` raises a TypeError.                                                       |
| 6-raise_exception_msg.py         | Function `raise_exception_msg` raises a NameError with a custom message.                              |
| 7-safe_print_integer_err.py      | Function `safe_print_integer_err` prints an integer value, returns True if printed correctly, False otherwise. Prints error message to stderr on failure. |
| 8-safe_function.py               | Function `safe_function` executes a function `fct` safely with provided *args. Returns result or prints and returns None on exception. |
| 9-magic_calculation.py           | Function `magic_calculation` replicates functionality from given Python bytecode.                    |

Authors : Baptiste POUQUEROU
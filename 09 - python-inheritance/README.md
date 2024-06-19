# Python - Inheritance

![1_xDlvgqeFbq_OHmR0WQH9bw](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/35f6fc03-d2af-4c79-b61e-3088cf7948e3)


**Completion:** 100%

**Title:** Python - Inheritance

**Level:** Master

**By:** Guillaume

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

## Resources

Read or watch:

- [Inheritance](https://example.com)
- [Multiple inheritance](https://example.com)
- [Inheritance in Python](https://example.com)
- [Learn to Program 10 : Inheritance Magic Methods](https://example.com)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

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
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Documentation

Do not use the words import or from inside your comments, the checker will think you are trying to import some modules.

| Filename                     | Description                                                                                           |
|------------------------------|-------------------------------------------------------------------------------------------------------|
| 0-lookup.py                  | Function `lookup(obj)` returns a list of available attributes and methods of an object.              |
| 1-my_list.py                 | Class `MyList` inherits from `list` with method `print_sorted(self)` to print sorted list.            |
| 2-is_same_class.py           | Function `is_same_class(obj, a_class)` returns True if obj is exactly an instance of a_class.          |
| 3-is_kind_of_class.py        | Function `is_kind_of_class(obj, a_class)` returns True if obj is an instance of or inherited from a_class. |
| 4-inherits_from.py           | Function `inherits_from(obj, a_class)` returns True if obj is an instance of a subclass of a_class.   |
| 5-base_geometry.py           | Empty class `BaseGeometry` defined.                                                                   |
| 6-geometry.py                | Class `BaseGeometry` with method `area(self)` raising an Exception indicating it's not implemented.   |
| 7-base_geometry.py           | Class `BaseGeometry` with method `integer_validator(self, name, value)` for validating integer values.|
| 8-rectangle.py               | Class `Rectangle` inheriting from `BaseGeometry` with width and height validated on instantiation.    |
| 9-rectangle.py               | Class `Rectangle` inheriting from `BaseGeometry` with `area()` method implemented and string representation defined. |
| 10-square.py                 | Class `Square` inheriting from `Rectangle` for squares with size instantiation.                       |
| 11-square.py                 | Class `Square` inheriting from `Rectangle` with custom string representation for squares.              |
| 100-my_int.py                | Class `MyInt` inheriting from `int` with inverted `==` and `!=` operators.                            |
| 101-add_attribute.py         | Function `add_attribute` adding a new attribute to an object if possible, raising `TypeError` if not. |


AUTHOR : BAPTISTE POUQUEROU

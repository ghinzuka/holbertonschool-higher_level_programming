# Classes and Objects


![wcXVeEw](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/f0806c87-00c0-4d4e-8a35-a2e7d7f08828)

**Completion:** 100%

**Title:** Python - Classes and Objects

**Level:** Amateur

**By:** Guillaume

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

## Background Context

It’s VERY important that you read at least all the material that is listed below (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

## Resources

Read or watch:

- [Object Oriented Programming](https://example.com) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
- [Object-Oriented Programming](https://example.com) (Please be careful: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
- [Properties vs. Getters and Setters](https://example.com)
- [Learn to Program 9 : Object Oriented Programming](https://example.com)
- [Python Classes and Objects](https://example.com)
- [Object Oriented Programming](https://example.com)

The above resources provide a mix of reading material, interactive exercises, and video tutorials to cater to different learning styles. It’s recommended to go through these resources to build a solid understanding of OOP concepts in Python before attempting the exercises.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

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
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

More Info
Documentation is now mandatory! Each module, class, and method must contain docstring as comments. Example Google Style Python Docstrings

| Filename                  | Description                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------|
| 0-square.py               | Empty class `Square` definition.                                                                 |
| 1-square.py               | Class `Square` with private instance attribute `size` and instantiation with a given size.       |
| 2-square.py               | Class `Square` with size validation in the constructor (`size` must be an integer >= 0).         |
| 3-square.py               | Class `Square` with public instance method `area()` to compute and return the area of the square. |
| 4-square.py               | Class `Square` with getter and setter methods for `size`, including validation for type and value. |
| 5-square.py               | Class `Square` extended with method `my_print()` to print the square using '#' symbols.           |
| 6-square.py               | Class `Square` enhanced with private instance attribute `position` and updated `my_print()` method. |
| 100-singly_linked_list.py | Node class for a singly linked list with `data` and `next_node` attributes.                      |
|                           | SinglyLinkedList class manages nodes and insertion in sorted order.                              |
| 101-square.py             | Class `Square` extended to support direct printing using `print()`, similar to `my_print()`.     |
| 102-square.py             | Class `Square` enhanced to support comparison operations (`==`, `!=`, `<`, `<=`, `>`, `>=`) based on area. |

AUTHOR : BAPTISTE POUQUEROU

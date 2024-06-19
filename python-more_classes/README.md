more classes
# More Classes and Objects

![Project Badge](badge-url)

**Completion:** 100%

**Title:** Python - More Classes and Objects

**Level:** Master

**By:** Guillaume

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

**Manual QA review must be done (request it when you are done with the project)**

## Resources

Read or watch:

- [Object Oriented Programming (Read everything until the paragraph “Inheritance” (excluded))](https://example.com)
- [Object-Oriented Programming (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)](https://example.com)
- [Class and Instance Attributes](https://example.com)
- [classmethods and staticmethods](https://example.com)
- [Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)](https://example.com)
- [str vs repr](https://example.com)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
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
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between an object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

| Filename               | Description                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------|
| 0-simple_rectangle.py  | Empty class `Rectangle` definition.                                                               |
| 1-real_definition.py   | Class `Rectangle` with private attributes (width and height), properties, and optional parameters. |
| 2-area_perimeter.py    | Extension of `Rectangle` class with methods `area()` and `perimeter()` for calculations.          |
| 3-string_representation.py | Modification of `Rectangle` class to include `__str__` and `__repr__` methods.                  |
| 4-eval_is_magic.py     | Enhancement of `Rectangle` class to support recreation using `eval(repr(rectangle))`.            |
| 5-detect_instance_deletion.py | Modification of `Rectangle` class to print a message upon instance deletion using `__del__`.  |
| 6-how_many_instances.py | Implementation of `Rectangle` class with `number_of_instances` class attribute tracking.         |
| 7-change_representation.py | Implementation of `Rectangle` class allowing changing print symbol with `print_symbol`.         |
| 8-compare_rectangles.py | Static method `bigger_or_equal(rect_1, rect_2)` to compare rectangles based on area.              |
| 9-square.py            | Extension of `Rectangle` class with class method `square(cls, size=0)` to create square instances.|

AUTHOR : BAPTISTE POUQUEROU
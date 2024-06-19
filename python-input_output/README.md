![python_input_and_output](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/0a0d5302-f8c9-40b6-bc64-9c9ec7d7e2f3)


**Completion:** 100%

**Title:** Python - Input/Output

**Level:** Amateur

**By:** Guillaume

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

## Resources

Read or watch:

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/reference/datamodel.html#object.__del__)
- [Dive Into Python 3: Chapter 11. Files](https://www.diveinto.org/python3/files.html) (until “11.4 Binary Files” (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://learnxinyminutes.com/docs/python3/)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
- [sys package](https://docs.python.org/3/library/sys.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
- How to access command line parameters in a Python script

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
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

This project will provide you with practical skills in handling input and output operations in Python, preparing you for more advanced topics in software development.


| Filename                   | Description                                                                                     |
|----------------------------|-------------------------------------------------------------------------------------------------|
| 0-read_file.py             | Reads a text file and prints its contents to stdout.                                             |
| 1-write_file.py            | Writes a string to a text file and returns the number of characters written.                     |
| 2-append_write.py          | Appends a string to the end of a text file and returns the number of characters added.           |
| 3-to_json_string.py        | Converts an object (list, dictionary, etc.) to its JSON representation as a string.              |
| 4-from_json_string.py      | Converts a JSON string back into a Python data structure (list, dictionary, etc.).                |
| 5-save_to_json_file.py     | Serializes an object (list, dictionary, etc.) into JSON format and saves it to a file.           |
| 6-load_from_json_file.py   | Loads JSON data from a file and reconstructs the original Python object.                         |
| 7-add_item.py              | Adds command-line arguments to a list, saves the list as JSON to a file.                         |
| 8-class_to_json.py         | Converts class instances with simple attributes to a JSON-serializable dictionary.               |
| 9-student.py               | Defines a Student class with attributes and a method that returns its JSON representation.       |
| 10-student.py              | Extends Student class with a method that optionally filters attributes based on a provided list. |
| 11-student.py              | Extends Student class with methods to save instance data to JSON file and reload from JSON data. |
| 12-pascal_triangle.py      | Generates Pascal's triangle up to a specified number of rows n.                                  |
| 100-append_after.py        | Inserts a new line after each occurrence of a specific string in a file.                         |
| 101-stats.py               | Reads logs, computes statistics on file size and status codes, and prints them every 10 lines.   |

Author : Baptiste PÖUQUEROU

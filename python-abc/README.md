# Python - Abstract Classes and Interfaces

![abstract-class-vs-interface](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/41964e77-f4cc-4ed5-a656-1bc0694b5108)

**Completion:** 100%

**Title:** Python - Abstract Classes and Interfaces

**Level:** Amateur

**By:** Javier Valenzani

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.

## Introduction

Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### Abstract Classes

- Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.

### Interfaces and Duck Typing

- Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.

### Subclassing Standard Base Classes

- Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.

### Method Overriding

- Employ method overriding to alter or enhance the behavior of base class methods.

### Multiple Inheritance

- Understand and apply multiple inheritance to form complex relationships between classes.

### Mixins

- Utilize mixins to compose behavior across unrelated classes.

## Resources

- [Python 3 Object-Oriented Programming](https://example.com)
- [ABC — Abstract Base Classes](https://example.com)
- [Real Python - Object-Oriented Programming (OOP) in Python 3](https://example.com)
- [Corey Schafer - OOP Playlist](https://example.com)
- [sentdex - Python OOP Tutorial](https://example.com)

The above resources provide a mix of reading material, interactive exercises, and video tutorials to cater to different learning styles. It’s recommended to go through these resources to build a solid understanding of OOP concepts in Python before attempting the exercises.

## TASKS

### Task 0: Abstract Animal Class and its Subclasses

- **Objective**: Create an abstract class named Animal using Python's ABC module with an abstract method `sound`. Implement two subclasses: Dog (sound = "Bark") and Cat (sound = "Meow").
- **Files**: `task_00_abc.py`, `main_00_abc.py`
- **Testing**: Example usage:
  ```python
  from task_00_abc import Animal, Dog, Cat

  bobby = Dog()
  garfield = Cat()

  print(bobby.sound())   # Expected Output: Bark
  print(garfield.sound())   # Expected Output: Meow
  ```
## Task 1: Shapes, Interfaces, and Duck Typing

- **Objective**: Create an abstract class named `Shape` with abstract methods `area` and `perimeter`. Implement two classes: `Circle` (radius-based) and `Rectangle` (width and height-based). Write a function `shape_info` to print the area and perimeter of any `Shape` object using duck typing.
- **Files**: `task_01_duck_typing.py`, `main_01_duck_typing.py`
- **Testing**: Example usage:
  ```python
  from task_01_duck_typing import Circle, Rectangle, shape_info

  circle = Circle(radius=5)
  rectangle = Rectangle(width=4, height=7)

  shape_info(circle)
  shape_info(rectangle)
  ```
  ## Task 2: Extending the Python List with Notifications

- **Objective**: Create a class named `VerboseList` that extends Python's built-in `list` class. Print notifications when items are added or removed using methods like `append`, `extend`, `remove`, and `pop`.
- **Files**: `task_02_verboselist.py`, `main_02_verboselist.py`
- **Testing**: Example usage:
  ```python
  from task_02_verboselist import VerboseList

  vl = VerboseList([1, 2, 3])
  vl.append(4)   # Expected Output: Added 4 to the list.
  vl.extend([5, 6])   # Expected Output: Extended the list with 2 items.
  vl.remove(2)   # Expected Output: Removed 2 from the list.
  vl.pop()   # Expected Output: Popped 6 from the list.
  vl.pop(0)   # Expected Output: Popped 1 from the list.
  ```
  ## Task 3: CountedIterator - Keeping Track of Iteration

- **Objective**: Create a class `CountedIterator` that extends Python's iterator to keep track of the number of items iterated. Implement methods to retrieve the count and override `__next__` to increment the count on each iteration.
- **Files**: `task_03_countediterator.py`, `main_03_countediterator.py`
- **Testing**: Example usage:
  ```python
  from task_03_countediterator import CountedIterator

  data = [1, 2, 3, 4]
  counted_iter = CountedIterator(data)

  try:
      while True:
          item = next(counted_iter)
          print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
  except StopIteration:
      print("No more items.")
	```

## Task 4: The Enigmatic FlyingFish - Exploring Multiple Inheritance

- **Objective**: Create a class `FlyingFish` that inherits from both `Fish` and `Bird` classes, demonstrating multiple inheritance. Override methods from both parents and explore method resolution order (MRO).
- **Files**: `task_04_flyingfish.py`, `main_04_flyingfish.py`
- **Testing**: Example usage:
  ```python
  from task_04_flyingfish import Fish, FlyingFish

  flying_fish = FlyingFish()
  flying_fish.swim()   # Expected Output: "The flying fish is swimming!"
  flying_fish.fly()   # Expected Output: "The flying fish is soaring!"
  flying_fish.habitat()   # Expected Output: "The flying fish lives both in water and the sky!"
	```
## Task 5: The Mystical Dragon - Mastering Mixins

- **Objective**: Design mixin classes `SwimMixin` and `FlyMixin` with `swim` and `fly` methods respectively. Create a `Dragon` class inheriting from both mixins to demonstrate multiple capabilities.
- **Files**: `task_05_dragon.py`, `main_05_dragon.py`
- **Testing**: Example usage:
  ```python
  from task_05_dragon import Dragon

  dragon = Dragon()
  dragon.swim()   # Expected Output: "The creature swims!"
  dragon.fly()   # Expected Output: "The creature flies!"
  dragon.roar()   # Expected Output: "The dragon roars!"
	```
AUTHOR : BAPTISTE POUQUEROU

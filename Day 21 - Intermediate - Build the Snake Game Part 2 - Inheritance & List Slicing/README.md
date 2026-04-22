# Day 21 - Build the Snake Game Part 2: Inheritance & List Slicing
___
## Concepts Practised
___
- Class Inheritance
- How to Slice Lists & Tuples in Python
___

```python
class Parent:
    def __init__(self):
        pass

# Inheritance
class Child(Parent):
    def __init__(self):
        # inherit from the super class. 
		super().__init__() # The call to super() in the initializer is recommended but not strictly required.
```
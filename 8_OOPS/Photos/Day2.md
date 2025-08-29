# 🔹 Classes & Objects in Python

## What is a Class?
- A **class** is like a **blueprint** for creating objects.  
- It defines **attributes (variables)** and **methods (functions)** that the objects will have.  

Example:  
```python
class Car:
    brand = "Toyota"   # attribute
    def drive(self):   # method
        return "The car is moving"

mycar = Car()        # creating an object
print(mycar.brand)   # accessing attribute
print(mycar.drive()) # calling method

```
## What is an Object?

- An object is an instance of a class.

- When you create an object, Python sets aside memory and gives you your own copy of the attributes.

```python

mycar = Car()        # creating an object
print(mycar.brand)   # accessing attribute
print(mycar.drive()) # calling method

```


# 🔹 The `__init__` Method in Python

## What is `__init__`?
- `__init__` is a **special constructor method** in Python.  
- It runs **automatically** whenever a new object is created.  
- It is used to **initialize (set up)** the object's data.  

---

## Example
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand     # setting up brand for the object
        self.color = color     # setting up color for the object

# Creating objects
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")

print(car1.brand, car1.color)  # Tesla Red
print(car2.brand, car2.color)  # BMW Black

```

# 🔹 The `self` Keyword in Python

- `self` refers to the **current instance of the class**.  
- It is used to **access attributes and methods inside the class**.  
- Python passes it **automatically**, but you must declare it as the first parameter in methods.  

## Example
```python
class Student:
    def __init__(self, name, age):
        self.name = name   # "self" attaches the value to the object
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

s1 = Student("Tony", 21)     # self → s1
s2 = Student("Ravi", 22)     # self → s2

print(s1.introduce())  # My name is Tony and I am 21 years old.
print(s2.introduce())  # My name is Ravi and I am 22 years old.

```


> Quick Recap

- Class → Blueprint.

- Object → Instance of a class.

- __init__ → Constructor, auto-calls when object is created.

- self → Refers to the current object, required in methods.
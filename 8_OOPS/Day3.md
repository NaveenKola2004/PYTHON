# Day 3: Instance Variables vs Class Variables

## 1. Instance Variables
- Belong to **individual objects** (instances).  
- Defined inside the `__init__` method using `self`.  
- Each object gets its **own copy** of the variable.  

### Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age       # instance variable

s1 = Student("Tony", 21)
s2 = Student("Alex", 22)

print(s1.name, s1.age)  # Tony 21
print(s2.name, s2.age)  # Alex 22
```

## 2. Class Variables

- Belong to the **class itself** (shared by all objects).  
- Defined **outside of `__init__`**, but inside the class.  
- Changing a class variable affects **all objects**, unless it’s overridden by an instance variable.  

### Example:
```python
class Student:
    college = "ABC University"   # class variable (shared)

    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age     # instance variable

s1 = Student("Tony", 21)
s2 = Student("Alex", 22)

print(s1.college)  # ABC University
print(s2.college)  # ABC University

# Change class variable
Student.college = "XYZ Institute"

print(s1.college)  # XYZ Institute
print(s2.college)  # XYZ Institute
```

## 3. Difference at a Glance

| Feature             | Instance Variable                       | Class Variable                         |
|--------------------|-----------------------------------------|----------------------------------------|
| Defined in          | Inside `__init__` with `self`          | Directly inside class, outside methods |
| Belongs to          | Each object (separate copy)            | The class (shared copy)                |
| Memory allocation   | Separate memory per object              | Single memory location for all objects |
| Example use case    | Student name, age, roll number          | School/college name, company name      |

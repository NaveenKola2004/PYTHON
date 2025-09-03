## The `__init__` Method (Constructor)

- `__init__` is a **special method** that automatically runs whenever a new object is created.  
- It is used to **initialize (set up)** object data.  
- Think of it as a **constructor** (like in Java or C++).  

### Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

# Create objects with unique data
s1 = Student("Tony", 21)
s2 = Student("Alex", 22)

print(s1.name, s1.age)  # Tony 21
print(s2.name, s2.age)  # Alex 22
```

## The `self` Keyword

- `self` refers to the **current instance of the class**.  
- It is used to **access attributes and methods** inside the class.  
- Python passes it automatically to methods — you just need to include it as the first parameter.  

### Example:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius   # instance variable

    def area(self):            # notice 'self' is the first parameter
        return 3.14 * (self.radius ** 2)

# Create objects
c1 = Circle(5)
c2 = Circle(7)

print(c1.area())  # 78.5
print(c2.area())  # 153.86
```


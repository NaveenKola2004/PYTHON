# What Is a Function?

- A function is like a mini-program inside your program.
It groups code that performs a specific task, so you can reuse it again and again.

> Example (without a function):
```python
print("Hello")
print("Welcome to python!")
```

> Example (With a function)
Now imagine doing that for 100 people... 😩
- Instead, write a function once and reuse it.
```python

def greet():
    print("Hello")
    print("Welcome to python!")
greet()

```

# ⚙️ Function Syntax

```python 

def function_name(parameters):
    # code block
    return something

```

1. def → keyword (tells Python you're defining a function)
2. function_name → your custom name
3. parameters → optional inputs (like variables)
4. return → gives back a value (optional)




# What is a Lambda Function?

- A lambda function is basically a small, anonymous function — meaning, it’s a function without a name.

> Instead of writing this:

```python
def (a,b):
    return a+b

```
>  You can write the same thing in one line using lambda:

```python

l=lambda a,b=a+b

```

> Boom 💥— no def, no return, no indentation. Just a quick, throwaway function.

### ⚙️ Syntax

```python

lambda arguments: expression
```
1. lambda → keyword
2. arguments → input values (like function parameters)
3. expression → single line of code that gets evaluated and returned


### 📦 Examples

```python 
square = lambda x: x * x
print(square(5))  # Output: 25

```
### Equivalent to:

```python

def square(x):
    return x * x

```

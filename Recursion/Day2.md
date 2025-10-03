## print the N numbers in using recursion

```python

def f(n):
    if(n==0):
        return
    sum=0
    sum=sum+n
    print(sum)
    f(n-1)
f(3)

```

### Print the sum of N numbers using the recursion 
> With using perameters

```python

def f(i,sum):
    if(i<1):
        print(sum)
        return
    f(i-1,sum+i)
f(3,0)

```

> solveing using the functional way sum of N numbers

```python
def f(n):
    if (n==0):
        return 0
    return n+f(n-1)
print(f(3))
```
> function way Factorial of a number

```python

def f(n):
    if(n==1):
        return n
    if(n==0):
        return 0
    return n*f(n-1)
print(f(5))

```

> Parameter way factorial of a number

```python

def f(i,fact):
    if(i==0):
        return 1
    if(i==1):
        print(fact)
        return
    f(i-1,fact*i)
print(f(6,1))

```

# A Deep Dive into Python Loops: `for` and `while`

This guide covers the essentials and advanced concepts of `for` and `while` loops in Python, designed to take you from basic syntax to idiomatic usage.

---

## `for` Loops — A Deep Dive 🔎

`for` loops are ideal for iterating over a sequence of items.

### Goal
Students should be able to:
* Explain how `for` works under the hood (the iterator protocol).
* Iterate over common iterables like lists, dictionaries, strings, files, ranges, and generators.
* Use common idioms like `enumerate`, `zip`, `reversed`, and `sorted`.
* Effectively use `break`, `continue`, and the `else` clause.

### Syntax
The basic structure is straightforward:
```python
for variable in iterable:
    # body of the loop
```

### How it Actually Works (Step-by-Step)
Under the hood, a `for` loop follows the **iterator protocol**:
1.  Python calls `iter(iterable)` on the object you're looping over. This returns an **iterator** object.
2.  It then repeatedly calls `next(iterator)` on that iterator to get the next item.
3.  When `next()` has no more items to return, it raises a `StopIteration` exception, and the loop gracefully terminates.

A rough "desugaring" of the process looks like this:
```python
# This is what Python does for you:
_it = iter(iterable) 
while True:
    try:
        variable = next(_it)
    except StopIteration:
        break
    # body of your loop
```

### Basic Examples
```python
# Looping over a list
for i in [10, 20, 30]:
    print(i)
# Output:
# 10
# 20
# 30

# Using range: range(start, stop, step)
# The 'stop' value is *exclusive*.
for i in range(1, 6):  # Iterates from 1 up to (but not including) 6
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
```

### Useful Built-ins & Idioms
* `enumerate(iterable, start=0)`: Gets both the index and the value.
    ```python
    names = ['alice', 'bob']
    for idx, name in enumerate(names, start=1):
        print(f"{idx}: {name}")
    # Output:
    # 1: alice
    # 2: bob
    ```

* `zip(a, b, ...)`: Iterates over multiple sequences in parallel. It stops when the shortest iterable is exhausted.
    ```python
    for a, b in zip([1, 2], ['x', 'y']):
        print(a, b)
    # Output:
    # 1 x
    # 2 y
    ```

* `dict.items()`: Iterates over key-value pairs in a dictionary.
    ```python
    d = {'a': 1, 'b': 2}
    for k, v in d.items():
        print(k, v)
    # Output:
    # a 1
    # b 2
    ```

* `reversed()` and `sorted()`: Control the iteration order without modifying the original list.
    ```python
    for x in reversed([1, 2, 3]):
        print(x) # 3, 2, 1

    for x in sorted(['c', 'a', 'b']):
        print(x) # a, b, c
    ```

### The `for-else` Clause
The `else` block runs **only if the loop completes normally** (i.e., it was not terminated by a `break` statement). This is incredibly useful for search operations.

**Example: Find the first divisor of a number**
```python
n = 17
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print(f"{n} is composite, first divisor is {i}")
        break
else:
    # This runs only if the loop finishes without a 'break'
    print(f"{n} is prime") 
```

### `break`, `continue`, and `pass`
* **`break`**: Exits the entire loop immediately.
* **`continue`**: Skips the rest of the current iteration and moves to the next one.
* **`pass`**: A placeholder that does nothing. It's used when syntax requires a statement but no action is needed.

### Nested Loops and Complexity
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```
Nested loops multiply the work. Two nested loops iterating over `n` items result in **O(n²)** complexity. Be mindful of performance!

### Mutating While Iterating — DON'T Do This ❌
Modifying a list while you are iterating over it can lead to unpredictable behavior, like skipping items.

**Bad Example:**
```python
lst = [1, 2, 3, 4]
for x in lst:
    if x % 2 == 0:
        lst.remove(x) # This will skip checking '3'!
```

**Safe Patterns:**
1.  Iterate over a **copy**: `for x in lst[:]`.
2.  Build a **new list** (often with a list comprehension): `new_list = [x for x in lst if x % 2 != 0]`.

### Generators & Files
`for` loops work seamlessly with generators and files because both are iterators. This is highly memory-efficient.

```python
# Generator example
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for f in fib(5):
    print(f) # 0, 1, 1, 2, 3

# File iteration example
with open('data.txt') as f:
    for line in f:  # Reads one line at a time into memory
        # process(line)
        pass 
```

---

## `while` Loops — A Deep Dive 🔄

`while` loops are used for condition-driven iteration, where the number of repetitions is not known beforehand.

### Goal
Students should be able to:
* Use `while` for condition-driven tasks.
* Avoid infinite loops and understand loop invariants.
* Implement common patterns like sentinel loops and `while-else`.

### Syntax
The condition is evaluated before each iteration. If it's `False` initially, the loop body never runs.
```python
while condition:
    # body of the loop
```

### Basic Example
```python
i = 0
while i < 5:
    print(i)
    i += 1
# Output:
# 0
# 1
# 2
# 3
# 4
```

### Common Patterns
* **Counting Loop**: Shown above, but a `for` loop is usually more Pythonic for simple counting.
* **Sentinel Loop**: A loop that runs until a special "sentinel" value is encountered. This is often implemented with `while True` and `break`.
    ```python
    while True:
        line = input("> ")
        if line == "quit":
            break
        print(f"You entered: {line}")
    ```
* **Do-While Emulation**: Python does not have a `do-while` loop, but you can emulate it with `while True` and a `break` at the end.
    ```python
    while True:
        # do something once
        # ...
        if not condition_to_continue:
            break
    ```

### `while-else`
The `else` clause works identically to `for-else`: it runs only if the loop terminates because its condition became `False`, not because of a `break`.

```python
i = 0
while i < 5:
    if check_something(i):
        # A condition was met, so we exit early
        break
    i += 1
else:
    # This runs only if the 'break' was never reached
    print("The condition was never met in any iteration.")
```

### Infinite Loop Caution ⚠️
A common bug is forgetting to update the variables that the loop condition depends on.
* To stop an infinite loop in a terminal, press **Ctrl+C**.
* Reason about a **loop invariant**: a condition that is true at the beginning of every iteration. This helps prove your loop is correct.

**Example: Euclid’s GCD Algorithm**
A classic `while` loop example. The loop continues as long as `b` is not zero.
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

---

## Suggested Teaching Plan 👨‍🏫

1.  **Warm-up (5 min)**: Quick quiz: What will `for i in range(3): print(i)` output?
2.  **`for` Syntax (7 min)**: Explain the syntax and live-code a simple list iteration.
3.  **Internals Demo (5 min)**: Show how `iter()` and `next()` work to demystify the `for` loop.
4.  **`enumerate` & `zip` (8 min)**: Give small tasks: index a list, pair two lists.
5.  **`for-else` Concept (5 min)**: Use the prime checking example to explain its utility.
6.  **`while` Intro (7 min)**: Show a counting example and a sentinel loop demo (`while True`).
7.  **Infinite Loops (3 min)**: Demonstrate an infinite loop and how to stop it (Ctrl+C).
8.  **Advanced Idioms (10 min)**: Cover generators, file iteration, and dictionary iteration.
9.  **Common Mistakes (10 min)**: Discuss mutating lists, off-by-one errors, and forgetting increments.
10. **Exercises (Homework)**: Assign the practice problems below.
11. **Q&A & Code Review**: Have students review each other's solutions.

---

## Practice Exercises (with Answers) ✏️

### `for`-Loop Exercises

1.  **Predict the output:**
    ```python
    for i in range(5, 0, -2):
        print(i)
    ```
    **Answer**:
    ```
    5
    3
    1
    ```

2.  **Use `enumerate` to print `1: alice`, `2: bob` from `['alice','bob']`.**
    **Solution**:
    ```python
    for idx, name in enumerate(['alice', 'bob'], 1):
        print(f"{idx}: {name}")
    ```

3.  **Flatten a matrix:** `[[1,2],[3,4]]` should become `[1,2,3,4]`.
    **Solution** (using a list comprehension, which is a concise `for` loop):
    ```python
    matrix = [[1, 2], [3, 4]]
    flat = [x for row in matrix for x in row]
    print(flat)
    ```

4.  **What happens when `zip` is used on lists of unequal lengths?**
    ```python
    for a, b in zip([1, 2, 3], ['x', 'y']):
        print(a, b)
    ```
    **Answer**: `zip` stops at the end of the shortest list. The output is:
    ```
    1 x
    2 y
    ```

### `while`-Loop Exercises

1.  **Use a `while` loop to compute the factorial of 5 (5! = 120).**
    **Solution**:
    ```python
    n = 5
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(result) # 120
    ```

2.  **Read numbers from the user until they enter 0, then print the sum.**
    **Solution**:
    ```python
    total = 0
    while True:
        num_str = input("Enter a number (or 0 to quit): ")
        n = int(num_str)
        if n == 0:
            break
        total += n
    print("Sum:", total)
    ```

3.  **Check if a string is a palindrome using a two-pointer `while` loop.**
    **Solution**:
    ```python
    s = "racecar"
    i, j = 0, len(s) - 1
    is_palindrome = True
    while i < j:
        if s[i] != s[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1
    print(is_palindrome) # True
    ```

---

## Common Pitfalls & How to Fix Them

* **Off-by-one with `range`**: Remember `range(n)` goes from `0` to `n-1`.
* **Mutating a list while iterating**: Iterate over a copy (`my_list[:]`) or build a new list.
* **Confusing `for-else`**: The `else` block runs only when there is **no `break`**.
* **Infinite `while` loops**: Always ensure the loop's condition will eventually become `False` or that there's a reachable `break`.
* **`zip` with different lengths**: `zip` truncates. If you need all elements, use `itertools.zip_longest`.

---

## Debugging Tips for Loops

* **Predict Output**: Before running, guess what the loop will do.
* **Use `print()`**: Add print statements inside the loop to track variables: `print(f"i={i}, item={item}")`.
* **Use a Debugger**: Use `pdb.set_trace()` or your IDE's debugger to step through the loop line by line.
* **Check for Mutation**: If items are being skipped, print the entire container at each iteration to see if it's changing unexpectedly.

---

## Quick Cheat-Sheet

```python
# for: Best when you know the items or are using iterables
for var in iterable:
    ...
else:
    # Runs if the loop didn’t break
    ...

# while: Best when repetition depends on a changing condition
while condition:
    ...
else:
    # Runs if the loop ended naturally (without break)
    ...

# --- Control Flow ---
break      # exit the entire loop immediately
continue   # skip to the next iteration
pass       # placeholder (no-op)
```

---

## Advanced Tips (for the Curious)

* **List Comprehensions**: Use `[f(x) for x in items]` for simple transformations. It's often faster than a standard `for` loop.
* **Generator Expressions**: Use `(x*x for x in items)` for lazy evaluation, which saves memory.
* **`itertools` module**: Explore this module for advanced iteration tools like `product`, `permutations`, `chain`, and `zip_longest`.
* **Performance**: Use the `timeit` module to measure the performance of different looping strategies for micro-optimizations.
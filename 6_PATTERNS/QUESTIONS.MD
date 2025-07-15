## 1. Right Angles Triangle
```python
* 
* * 
* * * 
* * * * 
```
<details><summary><strong>➡️ CODE</strong></summary>

```python
n=4
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
```
</details>

## 2. Flipped Right Angled Triangle
- Using '*'
- Input: n = 5

- Output:

```python
        *
      * *
    * * *
  * * * *
* * * * *
```
<details><summary><strong>➡️CODE</strong></summary>

```python
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
```
</details>

<details><summary>➡️USING NUMBERS AND ALPHABETS</summary>
- This same question they will ask the using numbers,and alphabets

```python 
      1
    1 2
  1 2 3
1 2 3 4

    A
  A B
A B C
```

- As same as the code just we chanege the code as the printing the '*' insted we will print the number and alphabet 
    - NUMBERS
        - just change the line 

   ```python
   print(k+1,end=" ")
   ```
   - ALPHABETS
        - In this we are using the ascii values
        - Using chr() print the alphabets
        - Small's 97 - 122
        - Captal's 65 -90
    ```python
    print(chr(64+i),end=" ")
</details>

## 3. Reversed Flipped Right Angled Triangle

- I this will be same as the above one we just changeing the staring point of first loop
- Using '*'
- Input: n = 4
- Output:

```python
* * * *
  * * *
    * *
      *
```

<details><summary><strong>➡️ CODE</strong></summary>

```python 
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
```

- Same as the numbers and alphabets printing reverse as we are see in the pervious one
</details>

## 4. Pyramid
- Using '*'
- Input: n = 4
- Output:
```python
      *
    * * *
  * * * * *
* * * * * * *
```
<details><summary><strong>➡️ CODE</strong></summary>

```python
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
```

- Numbers,Alphabets as we can do in previous codes change
</details>

## 5. Reverse Pyramid
```python
* * * * * * *
  * * * * *
    * * *
      *
```
<details><summary><strong>➡️ CODE</strong></summary>

```python
n=5
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
```
</details>

## 6. Diamond
```python
    *
  * * *
* * * * *
  * * *
    *
```

<details><summary><strong>➡️CODE</strong></summary>

```python
n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
```
</details>

## 7. Square

```python
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```

<details><summary><strong>➡️CODE</strong></summary>

```python
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
```
</details>


<details>
<summary><strong>Answer</strong></summary>

- n = numbers
- s= starting position
- ans = who will not out in this 
```python
def find(n,s):
    b=1
    while(b<=n):
        b=b*2
    b=b/2
    ans=(2*(n-b)+s)%n
    if (ans==0):
        return n
    else:
        return ans
print(int(find(5,5)))

```
</details>
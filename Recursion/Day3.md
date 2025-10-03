# 1. Check the polindrome of the string by using Recursion 
- in this for example consider as the MADAM
- In this we should take the in first one compare to the last one and the 2nd compare to the last to the before one this is the logic so for you should do 
- upto the the pointer of i reach the middle one like len()//2==i value 


<details>

<summary><strong> Code </strong></summary>

```python

def recursion_poli(i,s):
    if i>=len(s)//2:
        return True
    if s[i] !=s[len(s)-1-i]:
        return False
    return recursion_poli(i+1,s)
data=input()
Value=recursion_poli(0,data)
print(Value)

```

</details>


# 2. Print the Fibonacci sequence in using the multiple recursions 

<details>
<summary><strong>Code</strong></summary>

```python
def Fibonacci_sequence(n):
    if n<=1:
        return n
    return Fibonacci_sequence(n-1)+Fibonacci_sequence(n-2)
data=Fibonacci_sequence(4)
print(data)

```

</details>
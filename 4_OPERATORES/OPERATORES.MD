# OPERATORES

- Operators are symbols or words that tell the computer to do some kind of operation — usually with numbers, variables, or values.
- They many types of operator in python
- Each operator type and operator have some use in python

# TYPES OF OPERATORS

1. Arthmatic operator
2. Logical operator
3. Assignment operator
4. Comparision operator
5. Membership operator
6. identity operator
7. Bitwise operator
8. Boolean operator

<details>
<summary><strong>➡️ ARTHMATIC OPERATORS</strong></summary>

# ARTHMATIC OPERATORS

- This operator is well know for us.
- It is a mathamatical operators. 
- It perform the Addition,Subtraction,Multiplication,Division,Modulation we know very well.
- Additional operator is the FloorDivision and Exponentiation.
- FloorDivision 
   - It not return the . after value
   ```python
   print(154//3) #Output 51
   ```
- Exponention
   - it is like power of a number
   ```python
   print(2**2) #Output 4
   ```

|  OPERATOR        |      MEANING  |EXAMPLE      |
|------------------|---------------|-------------|
|  +        |Addition |2+2=4   |
|-|Subraction|10 - 2=8|
|*|Multiplication|5 * 2=10|
|/|Division|12%6=2|
|%|Modulation|12%6=0|
|//|FloorDivision|154//3 = 51|
|**|Exponention|2**2=4|
</details>
<details>
<summary><strong>➡️ LOGICAL OPERATORS</strong></summary>

| OPERATOR|EXAMPLE|
|---------|-------|
|and| 'A' and 'B' in "ABCD" -> True|
|or |'A' or 'B' in "ABCD" -> True|
|not|Reverse truth|
</details>
<details>
<summary><strong>➡️ ASSIGNMENT OPERATORS</strong></summary>

- This operator used to assign the values to the variable

|OPERATOR|MEANING|EXAMPLE|
|--------|-------|-------|
|=|Assign value to variable|a=20|
|+=|	Add and assign|	x += 3 → x = x + 3|
|-=|	Subtract and assign|	x -= 2|
|*=|	Multiply and assign|	x *= 4|
|/=|	Divide and assign|	x /= 2|
|//=|	Floor divide and assign	|x //= 2|
|%=|	Modulus and assign|	x %= 2|
|**=|	Exponent and assign|	x **= 3|
</details>
<details>
<summary><strong> ➡️ COMPARISION OPERATORS</strong></summary>

# COMPARISION OPERATORS

- It is used to compare the two operands.
- It return the only boolean value (True/False).


|OPERATOR|MEANING|EXAMPLE|
|--------|-------|-------|
|==|Equalto|3==3 -> True|
|!=|Not equalto|3!=2 -> True|
|<|LessThen|5<2 -> False|
|>|GraterThen|6>2 -> True|
|<=|LessThenEqualto|3<=3 ->True|
|>=|GraterThenEqualto|6>=5 ->True|
</details>
<details>
<summary><strong>➡️ MEMBERSHIP OPERATORS</strong></summary>

#  MEMBERSHIP OPERATORS

- Membership operator is defined in two types.
   - in
   - not in
- It return the boolean value.

| OPERATOR |EXAMPLE|
|----------|-------|
|in|b=["a"] a in b|
|not in |a=["b"] b not in a|

</details>

<details>
<summary><strong>➡️ IDENTITY OPERATORS</strong></summary>

# IDENTITY OPERATORS

- It checks two things are same

|Operator|	Meaning|	Example|
|--------|---------|--------|
|is|	Same object|	x is y|
|is not|	Not the same object|	x is not y|

</details>

<details><strong><summary>➡️ BOOLEAN OPERATOR</strong></summary>
- Bollean is represented as the TRUE/FALSE.
- In the python programming and the some other programming languages it represented most of (boll).
- Actually the boolean value True/False is came after we perform the comparision of two are more  Operands or Numbers.

### Example
```python
print(5>2) # Comparision between Numbers  ' TRUE '
a=10
b=9
print(a<b) # Comparision between operands  ' FALSE '
```
- In this most of used in the control flow statements we use this boolean operator.
- In python we can write the True like this, and Fasle like this
</details>

## Expersion

- It is the combination of operators and operands.

```python
a=78
b=90
x=a+b # -> This an expresion
print(x)
```
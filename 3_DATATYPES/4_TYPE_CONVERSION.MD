# TYPECONVERSION

- It means changing thir datatype 
- Actually we know the Number is int datatype & sequence of characture is string datatype so in python we can change thir type 
- It will applicable for any datatype
- It is two types 
  - Implicit Type Conversion (Automatic)
  - Explicit Type Conversion (manually)

<details>
<summary><strong> ➡️ IMPLICIT CONVERSION</strong></summary>

# IMPLICIT CONVERSION

- It is defined as the python automatically change their type

### Example
```python
a=89
b=1.9
c=a+b
print(c,type(c)) # 90.9 <class 'Float'>
```
</details>

<details>
<summary><strong>➡️ EXPLICIT CONVERSION </strong></summary>

# EXPLICIT CONVERSION

- We can convert the their type manually

- Common conversion functions:
   - int() – convert to integer

   - float() – convert to float

   - str() – convert to string

   - bool() – convert to boolean

   - list(), tuple(), set(), dict() – collections

```python
a=78
b=float(a)
c=87.9
d=int(c)
e="78"
f=int(e)
g=float(e)
print(a,b,c,d,e,f,g)
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))
```


## BOOLEAN (TYPE CONVERSION)

- It is some what different as compare to other conversion
- Actually boolean is return the True/False 
- Comming to type conversion ' Empty value and Zero is always False ' 
- We have any value it is True

```python 
a=""
b="Naveen"
c=0
d=89
e=99.9
print(bool(a),bool(b),bool(c),bool(d),bool(e))
```

</details>
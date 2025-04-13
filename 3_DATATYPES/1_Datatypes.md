
# DATA TYPES
- Datatypes are used to define the type of data to used to the variables in the code
- like we are used name , for that we use sequense of charactures that means string
   - example
    - name="Naveen"
## Types of Datatypes 

1. int(Interger)
2. str(String)
3. float(Float)
4. List,[ ]
5. tuple,( )
6. set,{ }
7. frozen set ,{ }
8. dict (dictionary),(key:values),{ }
9. Bool (True,False)


<details>
<summary><strong> ➡️ INT </strong></summary>

# INT (INTEGER)

1. interger means number
2. All the whole numbers

```python 
myNumber1=78
myNumber2=-12
```
</details>

<details>
<summary><strong> ➡️ STRING </strong></summary>

# Str (STRING)

1. string is defined as the sequense of charactures
2. Enclosed with the single ' ' OR Double "  " queatations
3. It as the some methods 
4. we can Get the all types of methods by using this line of code
```python 
print(dir("str"))
```
- String is Mutable 
- Support the 
  - add
  - update
  - delete
- String is ordered
- Support the Indexing and Slicing
- Allow the duplicate values

5. String is starting with the 0 for front side
6. For Back side starting with -1
```python
 N   A  V  E  E  N
 0   1  2  3  4  5
-6  -5 -4 -3 -2 -1
```

7. Indexing
```python 
x="python"
print(x[0]) #Output p
print(x[-1]) #Output n
```
8. Slicing
```python 
x="Naveen"
print(x[0:5]) #Output Navee
print(x[-4:-1]) #Output vee
```
- It this we are giving the [Start : Stop :step]
-  For Stop it will take the you entered the 5 it will take the 4 only it take the Stop as the previous number of you entered number
- Step is skiping the numbers
```python 
x="Naveen"
print(x[::-1]) #Output neevaN
```
- Working of the Step you type the [: : -1] we are not provide the stop and stop we just provide the step so it will go and visit each characture and print it

```python 
N     A     V       E       E       N
0                                  -1
```

- step is [ : :-2] starting 1 and ending is upto end of string and step is -2
```python 
N     A     V       E       E       N   #Output  NEA
                   -2      -1       0
     -2    -1       0
-1    0
```

9. Make practice on the each method in the string

10. Formulas for slicing 
```python
i=start+n⋅step
If step > 0: loop while i < stop

If step < 0: loop while i > stop
```
</details>
<details>
<summary> <strong> ➡️ FLOAT  </strong></summary>
# Float

1. Float is a decimal values it contains the point values
- example
   - 1.2
   - -9.8
2. Like that we can define the float values

</details>

<details>
<summary><strong> ➡️ LIST </strong></summary>

# LIST(  [  ]  )

- List is collection of any type of values(data)
- It is enclosed with the square brackets ( [  ] )
- List is mutable so it supports the 
  - Add
  - Update
  - Delete
- It ordered also so it supports the 
  - Indexing
  - Slicing
- Allow duplicate values also

### Creating the list

- creating the Empty list
```python 
Fruits=[]
print(type(Fruits))
```
-  inserting the String data

```python 
Fruits=["APPLE","BANANA","GRAPES"]
print(Fruits) #Output ['APPLE', 'BANANA', 'GRAPES']
```
- Inserting the Numeric data

```python 
Numbers=[1,2,3,4,0,-1,7.98,89]
print(Numbers) #Output [1, 2, 3, 4, 0, -1, 7.98, 89]
```

- inserting the all types of data

```python
Data=["naveen",18,99.9,-100,10/8]
print(Data) # ['naveen', 18, 99.9, -100, 1.25]

```
- So this all are the Creating list and inserting data to the list and geting the data

### Acessing the each data

- So it would be the Ordered so supports the Indexing & Slicing to we can acessing each elements

#### Indexing

- Indexing same as string Starting with ' 0 '
- In string we get the each characture
- In List we get the each Element

```python 
Fruits=["APPLE","BANANA","GRAPES"]
print(Fruits[0]) #Output  APPLE
print(Fruits[-1]) #Output GRAPES
```

#### Slicing [START : STOP  : STEP ]

- Slicing is same as String 

```python
Fruits=["APPLE","BANANA","GRAPES"]
print(Fruits[0:3]) #Output ["APPLE","BANANA","GRAPES"]
print(Fruits[-3:-1]) #Output ["APPLE","BANANA"]
print(Fruits[::-1]) #Output ["GRAPES","BANANA","APPLE"]
```
- As String as Methods List also have the methods
- We can get the methods

```python 
Fruits=[]
print(dir(Fruits))
```
- Make practice on the each method in the LIST 
</details>

<details>
<summary><strong> ➡️ TUPLE</strong></summary>

# TUPLE 

1. Tuple is collection of any type of data
2. It is enclosed with the '  (  )  '
3. Tuple is immutable 
   - it is not support the add,update,delete the values in tupe
4. It is ordered
   - It is support the Indexing & Slicing
5. Allow the duplicate values

### Creating empty Tuple

```python
Fruits=()
print(type(Fruits)) #<class 'Tuple'>
```
#

### Inserting values to Tuple

```python
Fruits=("APPLE","ORANGE","GRAPE") 
print(Fruits) #Output ("APPLE","ORANGE","GRAPE")
```

### Indexing

```python
Fruits=("APPLE","ORANGE","GRAPE")
print(Fruits[0]) #Output APPLE
```
### Slicing

```python 
Fruits=("APPLE","ORANGE","GRAPE")
print(Fruits[::-1])  #Output ('GRAPE','ORANGE','APPLE')
```
-  Slicing and Indexing same as list

### Methods

- Get the all method of tuple like this 

```python
Fruits=()
print(dir(Fruits))
```

- Practice the each method on Tuple
</details>

<details>
<summary><strong>➡️ SET</strong></summary>

# SET '  { }  '

1. Set is mutable
   - Add
   - Update
   - Delete
2. It is unorderd
  - Not support the indexing and slicing
3. Stores immutable data
4. Not allow the store the duplicate values
   - it will take but not shown in result
5. It stores only immutable data
   - Liske tuple data like that immutable data

### Creating Set

```python
Fruits={"naveen"}
Names=set()
print(type(Fruits)) #Output <class 'set'>
print(type(Names))  #Output <class 'set'>
```
### Stores only Immutable data

```python
Names={"naveen",18,(99,89,78)}
print(Names) #Output {'Naveen', 18, (99, 89, 78)}
```
```python
Names={"Naveen",18,[99,89,78]}
print=(Names) # type error unhashable type: 'list'
```
### Methods 

```python
Name=set()
print(dir(Name))
```
</details>

<details>
<summary><strong>➡️ FROZEN SET</strong></summary>

# FROZEN SET

- It is immutable 
- It is Unordered
- Not allow the duplicate
- Stores only immutable data

### Creating Frozenset 

```python
Names=frozenset()
print(type(Names)) # <class 'frozenset'>
```
### Creating Frozenset with mutable data values

```python
Names=frozenset(["naveen",456])
print(Names) #Output frozenset({456,'Naveen'})
```
### Creating Frozenset with immutable data values

```python
Names=frozenset("naveen")
print(Names) #Output frozenset({'n','a','v','e'})
```
### Methods

- We can get the frozenset methods 

```python
Names=frozenset()
print(dir(Names))
```

</details>

<details>
<summary> <strong>➡️ DICTIONARY </strong></summary>

# DICTIONARY (dict)

- Dictionary is mutable
   - Add
   - Update
   - Delete
- Data in the form of {Key : values}
- Accessing elements by key 
- it is not support indexing and slicing
- It allow duplicate values 
- But Keys should be UNIQUE
- Not allow duplicate keys

### Creating dictionary

```python
Names={}
Address=dict()
print(type(Names)) #<class 'dict'>
print(type(Address)) #<class 'dict'>
```
### Creating dictionary with values

```python
Names={1:"Kola",2:"Naveen"}
print(Names)  #Output {1:"Kola",2:"Naveen"}
```

### Accessing elements by key

```python
Names={1:"Kola",2:"Naveen"}
print(Names[1])  #Output kola
```

### Methods of dictionary

```python
Names=dict()
print(dir(Names))
```

</details>
<details>
<summary><strong> ➡️ BOOLEAN</strong></summary>

# BOOLEAN (BOOL) 

- Boolean is represented as the True or False
- We write Bool in the pyhton True and False
- Don't change the cases because it has meaning in python

```python
print(5>6) #Output False
print(5<6>) #Output True
```
</details>

## Operations on Datatypes

| Operation            | List   | Tuple  | Set                    | FrozenSet              | Dictionary           |
|----------------------|--------|--------|------------------------|------------------------|----------------------|
| Adding elements      | ✅ Yes | ❌ No  | ✅ Yes                 | ❌ No                  | ✅ Yes               |
| Accessing elements   | ✅ Yes | ✅ Yes | ⚠️ No direct indexing | ⚠️ No direct indexing | ✅ Yes (by key)      |
| Updating elements    | ✅ Yes | ❌ No  | ✅ Yes                 | ❌ No                  | ✅ Yes               |
| Deleting elements    | ✅ Yes | ❌ No  | ✅ Yes                 | ❌ No                  | ✅ Yes               |

# Practice and solve the Assignments
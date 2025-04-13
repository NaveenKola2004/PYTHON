- Actually we have some format specifiers 
- I suggest you to use the F strings

- printing the string we just write the string inside of parenthises
```python
a="Naveen"
print("Hello,Wolrd!")
print(a)
```
- it will print the Hello,world! after Naveen in next line it will print
- but i want Naveen should between the Hello,World!
- Here we can use the f strings

```python
a="Naveen"
print(f"Hello,{a} World!")  # Hello,Naveen World!
```
- we should remenber two things
  1. First put the f starting
  2. We can use the { } to define the variable name inside of the brackets
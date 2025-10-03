Here is a comprehensive set of over 100 practice questions covering **Variables, Data Types, Type Conversion, and Conditional Statements**. The examples use a Python-like syntax, but the concepts apply to most programming languages.

***

## Variables

This section covers declaring variables, naming rules, and assigning values.

#### Identify Valid & Invalid Variable Names

For each of the following, state whether it is a **valid** or **invalid** variable name.

1.  `my_variable`
2.  `1st_variable`
3.  `my-variable`
4.  `variable1`
5.  `_variable`
6.  `$variable`
7.  `variable name`
8.  `Variable`
9.  `for` (assuming it's a keyword)
10. `__init__`

#### What is the Output?

Predict the output of the following code snippets.

11. ```python
    x = 10
    print(x)
    ```
12. ```python
    name = "Alice"
    name = "Bob"
    print(name)
    ```
13. ```python
    a = 5
    b = a
    a = 10
    print(b)
    ```
14. ```python
    score = 100
    score = score + 10
    print(score)
    ```
15. ```python
    x = 2
    y = 5
    x = y
    print(x)
    ```

#### Write the Code

16. Declare a variable named `age` and assign your age to it.
17. Declare a variable named `city` and assign the name of your city to it.
18. Create a variable `price` with a value of `50`. Then, update the value of `price` to `75`.
19. Create two variables, `first_name` and `last_name`, and assign your names to them.
20. Declare a variable `is_learning` and assign a boolean value (`True` or `False`) to it.
21. Create a variable `x` with value `10` and a variable `y` with value `20`. Write code to swap their values.
22. Declare a variable `pi_value` and assign the value `3.14` to it.
23. Create a variable `total_cost` and calculate it by adding two other variables, `item1_price` (value: 200) and `item2_price` (value: 300).
24. Declare a variable `user_email` and store a sample email address in it.
25. Create a variable `count` and initialize it to `0`. Then, write a line of code to increase its value by `1`.

***

## Data Types

This section focuses on identifying and using fundamental data types like integers, floats, strings, and booleans.

#### Identify the Data Type

What is the data type of the value in each statement? (e.g., Integer, Float, String, Boolean)

26. `user_id = 101`
27. `temperature = 98.6`
28. `greeting = "Hello, World!"`
29. `is_active = True`
30. `quantity = "25"`
31. `pi = 3.14159`
32. `error_code = -1`
33. `status_message = ''` (an empty string)
34. `user_exists = False`
35. `height = 182.0`

#### What is the Output?

Predict the output of the following code snippets.

36. `print(type(42))`
37. `print(type("42"))`
38. `print(type(42.0))`
39. `print(type(False))`
40. `print(type("True"))`
41. `x = 0; print(type(x))`
42. `y = "0"; print(type(y))`
43. `z = 0.0; print(type(z))`

#### Write the Code

44. Create a variable named `item_count` that holds an integer value.
45. Create a variable named `account_balance` that holds a floating-point number.
46. Create a variable named `user_message` that holds a string.
47. Create a variable named `is_complete` that holds a boolean value.
48. Create a variable `phone_number` and store a phone number as a string (since it might contain characters like '+').
49. Create a variable `product_id` and store `404` as a string.
50. Create a variable `discount_rate` and store `0.15` as a float.

***

## Type Conversion (Casting)

This section includes questions on converting one data type to another.

#### What is the Output?

Predict the output of the following code snippets. If it produces an error, write "Error".

51. `print(int("250"))`
52. `print(str(100))`
53. `print(float("99.9"))`
54. `print(int(54.8))`
55. `print(float(77))`
56. `print(int("Hello"))`
57. `print(str(True))`
58. `print(int(True))`
59. `print(int(False))`
60. `print(bool(0))`
61. `print(bool(1))`
62. `print(bool(-10))`
63. `print(bool(""))`
64. `print(bool("any text"))`
65. `x = "10"; y = "20"; print(x + y)`
66. `x = "10"; y = 20; print(int(x) + y)`
67. `a = 5.5; b = " apples"; print(str(a) + b)`
68. `print(int("10.5"))`

#### Write the Code

69. A variable `num_as_string` holds the value `"45"`. Convert it to an integer and store it in a variable called `num_as_int`.
70. A variable `current_year` holds the integer `2025`. Convert it to a string to be used in a message.
71. You get user input for their age, which is always a string. Write code to take an input `user_age_str` (e.g., `"21"`) and convert it to an integer.
72. Create a message `Welcome, user 123!` by concatenating the string `"Welcome, user "` and the integer `123`.
73. A variable `total` has the value `150`. A variable `count` has the value `"3"`. Calculate the average by first converting `count` to an integer.
74. Given `score = "500"`, convert it to a float.
75. Given `is_logged_in = 1` (an integer), convert it to a boolean.

***

## Conditional Statements

This section tests your knowledge of `if`, `elif` (else if), and `else`, along with comparison and logical operators.

#### Predict the Output

What will be printed to the console for each code block?

76. ```python
    age = 20
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
    ```
77. ```python
    temp = 15
    if temp > 25:
        print("It's hot.")
    else:
        print("It's not hot.")
    ```
78. ```python
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")
    ```
79. ```python
    x = 10
    y = 10
    if x == y:
        print("Equal")
    else:
        print("Not Equal")
    ```
80. ```python
    is_sunny = True
    is_warm = False
    if is_sunny and is_warm:
        print("Go to the beach")
    else:
        print("Stay home")
    ```
81. ```python
    has_ticket = True
    has_popcorn = False
    if has_ticket or has_popcorn:
        print("Ready for the movie")
    else:
        print("Not ready")
    ```
82. ```python
    is_admin = False
    if not is_admin:
        print("Access Denied")
    else:
        print("Access Granted")
    ```
83. ```python
    num = 0
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
    ```
84. ```python
    grade = 'B'
    if grade == 'A' or grade == 'B':
        print("Good job!")
    else:
        print("Keep trying!")
    ```
85. ```python
    speed = 60
    is_birthday = True
    if speed < 31 or (is_birthday and speed < 36):
        print("No ticket")
    else:
        print("Ticket")
    ```

#### Write the Code

86. Write a program that checks if a number is positive. If it is, print "Positive".
87. Write a program that checks if a user is eligible to vote. The legal age is 18. Print "Eligible" or "Not Eligible".
88. Write code that checks if a number is even or odd. Print "Even" or "Odd" accordingly. (Hint: use the modulo operator `%`).
89. Write a program that takes a variable `day_of_week` (e.g., "Monday") and prints "It's a weekday" or "It's the weekend".
90. Write a program to find the largest of two numbers.
91. Write a program that assigns a letter grade based on a score:
    * 90-100: "A"
    * 80-89: "B"
    * 70-79: "C"
    * Below 70: "F"
92. Write code that checks if a password string is longer than 8 characters. Print "Strong password" or "Weak password".
93. Write code that checks if a variable `username` is empty. If it is, print "Username cannot be empty".
94. Write a program that checks if a year is a leap year. (A leap year is divisible by 4, except for end-of-century years, which must be divisible by 400).
95. Write a program for a simple login system. If the `username` is "admin" and the `password` is "12345", print "Login successful", otherwise print "Login failed".
96. Check if a number is between 1 and 100 (inclusive).
97. A store offers a discount if the purchase amount is over 1000. Write code that checks `purchase_amount` and prints "Discount applied" or "No discount".
98. Write a program that checks if a variable `letter` is a vowel (`a, e, i, o, u`).
99. Write a program that checks if a temperature is within the range of 20 to 30 degrees Celsius. Print "Comfortable" if it is, and "Uncomfortable" if it isn't.
100. Write a nested `if` statement. First, check if a person `has_license`. If true, then check if their `age` is over 25. If both are true, print "Can rent a car".
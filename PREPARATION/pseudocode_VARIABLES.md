```plaintext
=============================================
     10 PSEUDOCODE EXAMPLES: VARIABLES
=============================================

-- 1. Declaring and Initializing a Variable
-- A variable is a named storage location.
BEGIN
  DECLARE age AS INTEGER
  SET age = 25
  PRINT "The age is: " + age
END



-- 2. Storing User Input
-- Variables hold data provided by the user.
BEGIN
  DECLARE userName AS STRING
  PRINT "Please enter your name:"
  GET userName
  PRINT "Hello, " + userName
END




-- 3. Performing a Calculation
-- Variables are used to store numbers for operations.
BEGIN
  DECLARE length AS INTEGER = 10
  DECLARE width AS INTEGER = 5
  DECLARE area AS INTEGER

  SET area = length * width
  PRINT "The area is: " + area
END



-- 4. Updating a Variable (Counter)
-- The value stored in a variable can be changed.
BEGIN
  DECLARE counter AS INTEGER = 0
  PRINT "Initial count: " + counter

  SET counter = counter + 1
  PRINT "Updated count: " + counter
END





-- 5. Storing a Boolean (True/False)
-- Variables can hold logical states.
BEGIN
  DECLARE isLoggedIn AS BOOLEAN
  SET isLoggedIn = true

  IF isLoggedIn IS true THEN
    PRINT "User is logged in."
  ELSE
    PRINT "User is not logged in."
  END IF
END





-- 6. Swapping the Values of Two Variables
-- A temporary variable is often needed to swap values.
BEGIN
  DECLARE a AS INTEGER = 10
  DECLARE b AS INTEGER = 20
  DECLARE temp AS INTEGER

  PRINT "Before swap: a = " + a + ", b = " + b

  SET temp = a
  SET a = b
  SET b = temp

  PRINT "After swap: a = " + a + ", b = " + b
END




-- 7. Concatenating Strings
-- Variables can hold text that can be joined together.
BEGIN
  DECLARE firstName AS STRING = "Tony"
  DECLARE lastName AS STRING = "Stark"
  DECLARE fullName AS STRING

  SET fullName = firstName + " " + lastName
  PRINT "Full name: " + fullName
END




-- 8. Storing a Floating-Point Number
-- Variables can store numbers with decimal points.
BEGIN
  DECLARE price AS FLOAT = 19.99
  DECLARE taxRate AS FLOAT = 0.08
  DECLARE totalCost AS FLOAT

  SET totalCost = price + (price * taxRate)
  PRINT "The total cost is: " + totalCost
END



-- 9. Using a Variable in a Loop
-- A variable can control the flow of a loop.
BEGIN
  DECLARE loopCounter AS INTEGER

  FOR loopCounter FROM 1 TO 5
    PRINT "This is loop number: " + loopCounter
  ENDFOR
END




-- 10. Calculating an Average
-- Multiple variables work together to solve a problem.
BEGIN
  DECLARE num1, num2, num3 AS INTEGER
  DECLARE sum, average AS FLOAT

  PRINT "Enter first number:"
  GET num1
  PRINT "Enter second number:"
  GET num2
  PRINT "Enter third number:"
  GET num3

  SET sum = num1 + num2 + num3
  SET average = sum / 3.0

  PRINT "The average is: " + average
END

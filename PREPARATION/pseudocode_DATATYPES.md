```
-- ===================================================
--      20 PSEUDOCODE EXAMPLES: DATA TYPES
-- ===================================================

-- ### Primitive Data Types in Action ###

-- 1. Long Integer (LONG_INTEGER)
BEGIN
  DECLARE worldPopulation AS LONG_INTEGER
  SET worldPopulation = 8100000000
  PRINT "The approximate world population is: " + worldPopulation
END

-- 2. Double Precision Float (DOUBLE)
BEGIN
  DECLARE pi_value AS DOUBLE
  SET pi_value = 3.141592653589793
  PRINT "A precise value of Pi is: " + pi_value
END

-- 3. String Operation (Length)
BEGIN
  DECLARE message AS STRING = "Hello"
  DECLARE messageLength AS INTEGER
  SET messageLength = LENGTH(message)
  PRINT "The word 'Hello' has " + messageLength + " characters."
END

-- 4. Character to Integer Conversion (ASCII/Unicode)
BEGIN
  DECLARE letter AS CHAR = 'A'
  DECLARE asciiValue AS INTEGER
  SET asciiValue = CONVERT_TO_INTEGER(letter)
  PRINT "The ASCII value of 'A' is " + asciiValue
END

-- 5. Boolean from a Comparison
BEGIN
  DECLARE age AS INTEGER = 20
  DECLARE isAdult AS BOOLEAN
  SET isAdult = (age >= 18)
  PRINT "Is the person an adult? " + isAdult
END


-- ### Structured Data Types ###

-- 6. 2D Array (Matrix)
BEGIN
  DECLARE ticTacToeBoard AS ARRAY[3][3] OF CHAR
  SET ticTacToeBoard[0][0] = 'X'
  SET ticTacToeBoard[1][1] = 'O'
  PRINT "Center square has: " + ticTacToeBoard[1][1]
END

-- 7. Record / Struct
BEGIN
  DEFINE RECORD Student
    studentID AS INTEGER
    name AS STRING
    gpa AS FLOAT
  END RECORD

  DECLARE student1 AS Student
  SET student1.name = "Tony"
  SET student1.gpa = 3.8
  PRINT student1.name + " has a GPA of " + student1.gpa
END

-- 8. Array of Records
BEGIN
  -- Assumes the Student record from #7 is defined
  DECLARE classRoster AS ARRAY OF Student
  -- (Code to add multiple students to the roster would go here)
  PRINT "This is an array of student records."
END

-- 9. Enumeration (Enum)
BEGIN
  DEFINE ENUM DaysOfWeek {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY}
  DECLARE today AS DaysOfWeek
  SET today = DaysOfWeek.TUESDAY
  PRINT "Today is " + today
END

-- 10. Dictionary / Map
BEGIN
  DECLARE phonebook AS DICTIONARY OF STRING:STRING
  SET phonebook["Tony"] = "555-0101"
  SET phonebook["Steve"] = "555-0102"
  PRINT "Tony's number is: " + phonebook["Tony"]
END

-- 11. Set
BEGIN
  DECLARE uniqueTags AS SET OF STRING
  ADD "programming" TO uniqueTags
  ADD "data" TO uniqueTags
  ADD "programming" TO uniqueTags -- This duplicate is ignored
  PRINT "Number of unique tags: " + COUNT(uniqueTags)
END

-- 12. Tuple
BEGIN
  DECLARE coordinates AS TUPLE (INTEGER, INTEGER, STRING)
  SET coordinates = (10, 20, "Origin")
  PRINT "The point is at (" + coordinates[0] + ", " + coordinates[1] + ")"
END


-- ### Advanced Concepts & Type Interactions ###

-- 13. Constant (CONSTANT)
BEGIN
  DECLARE CONSTANT PI AS FLOAT = 3.14159
  -- SET PI = 4.0 // This would cause an error
  PRINT "The value of PI is always " + PI
END

-- 14. User-Defined Type
BEGIN
  DEFINE RECORD Point
    x AS INTEGER
    y AS INTEGER
  END RECORD

  DECLARE startPoint AS Point
  SET startPoint.x = 0
  SET startPoint.y = 0
END

-- 15. Date/Time Data Type
BEGIN
  DECLARE today AS DATETIME
  SET today = CURRENT_DATE()
  PRINT "Today's date is " + today
END

-- 16. Type Inference (Dynamic Typing)
BEGIN
  DECLARE value = 42       // Inferred as INTEGER
  PRINT "Value is an integer."
  
  SET value = "Hello"    // Now inferred as STRING
  PRINT "Value is now a string."
END

-- 17. String to Number Array Conversion
BEGIN
  DECLARE numString AS STRING = "5,10,15"
  DECLARE numArray AS ARRAY OF INTEGER
  SET numArray = SPLIT(numString, ",")
  PRINT "The first number is " + numArray[0]
END

-- 18. Function Declared with a Return Type
BEGIN
  FUNCTION Add(a AS INTEGER, b AS INTEGER) RETURNS INTEGER
    RETURN a + b
  ENDFUNCTION

  DECLARE sum AS INTEGER
  SET sum = Add(5, 7)
  PRINT "The result is " + sum
END

-- 19. Procedure Accepting Multiple Data Types
BEGIN
  PROCEDURE DisplayUser(name AS STRING, age AS INTEGER)
    PRINT "User: " + name + ", Age: " + age
  END PROCEDURE

  CALL DisplayUser("Tony", 25)
END

-- 20. Void / No Return Type
BEGIN
  PROCEDURE LogMessage(message AS STRING) RETURNS VOID
    PRINT "LOG: " + message
  END PROCEDURE

  CALL LogMessage("System starting up.")
END
```
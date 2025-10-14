
```
-- =============================================
--      10 PSEUDOCODE EXAMPLES: OPERATORS
-- =============================================

-- 1. Arithmetic Operators (+, -, *, /)
-- Used for mathematical calculations.
BEGIN
  DECLARE a AS INTEGER = 10
  DECLARE b AS INTEGER = 3
  
  PRINT "Addition: " + (a + b)      // Result: 13
  PRINT "Subtraction: " + (a - b)   // Result: 7
  PRINT "Multiplication: " + (a * b) // Result: 30
  PRINT "Division: " + (a / b)      // Result: 3
END


-- 2. Modulus Operator (MOD or %)
-- Gives the remainder of a division.
BEGIN
  DECLARE total_items AS INTEGER = 25
  DECLARE items_per_box AS INTEGER = 7
  DECLARE leftover_items AS INTEGER

  SET leftover_items = total_items MOD items_per_box
  
  PRINT "Leftover items: " + leftover_items // Result: 4
END


-- 3. Relational Operator: Equal To (==)
-- Compares two values to see if they are equal.
BEGIN
  DECLARE password_attempt AS STRING = "12345"
  DECLARE correct_password AS STRING = "54321"

  IF password_attempt == correct_password THEN
    PRINT "Access Granted."
  ELSE
    PRINT "Access Denied."
  END IF
END


-- 4. Relational Operator: Greater Than (>)
-- Checks if the left value is greater than the right value.
BEGIN
  DECLARE user_age AS INTEGER = 21
  DECLARE minimum_age AS INTEGER = 18

  IF user_age > minimum_age THEN
    PRINT "You are old enough to enter."
  ELSE
    PRINT "You are not old enough."
  END IF
END


-- 5. Logical Operator: AND
-- Checks if BOTH conditions are true.
BEGIN
  DECLARE has_ticket AS BOOLEAN = true
  DECLARE has_id AS BOOLEAN = false

  IF has_ticket AND has_id THEN
    PRINT "Allowed to board."
  ELSE
    PRINT "Cannot board. Missing ticket or ID."
  END IF
END


-- 6. Logical Operator: OR
-- Checks if AT LEAST ONE condition is true.
BEGIN
  DECLARE has_coupon AS BOOLEAN = true
  DECLARE is_member AS BOOLEAN = false

  IF has_coupon OR is_member THEN
    PRINT "Discount applied."
  ELSE
    PRINT "No discount available."
  END IF
END


-- 7. Logical Operator: NOT
-- Reverses a boolean value (true becomes false, false becomes true).
BEGIN
  DECLARE is_door_locked AS BOOLEAN = false

  IF NOT is_door_locked THEN
    PRINT "Please lock the door."
  END IF
END


-- 8. Assignment Operator (=)
-- Assigns a value to a variable.
BEGIN
  DECLARE score AS INTEGER = 0 // Initial assignment
  PRINT "Score: " + score

  SET score = 100 // Re-assignment
  PRINT "New Score: " + score
END


-- 9. Concatenation Operator (+)
-- Joins strings together.
BEGIN
  DECLARE greeting AS STRING = "Hello"
  DECLARE subject AS STRING = "World"
  
  DECLARE message AS STRING = greeting + ", " + subject + "!"
  
  PRINT message // Result: "Hello, World!"
END


-- 10. Increment Operator (++)
-- Shorthand for increasing a number by one.
BEGIN
  DECLARE like_count AS INTEGER = 99
  
  INCREMENT like_count // Equivalent to: SET like_count = like_count + 1
  
  PRINT "Total likes: " + like_count // Result: 100
END
```
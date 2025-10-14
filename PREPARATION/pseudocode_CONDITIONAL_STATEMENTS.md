```pseudocode
-- ===================================================
--   COMPREHENSIVE PSEUDOCODE GUIDE FOR PLACEMENTS
-- ===================================================

-- ### PROGRAMMING FUNDAMENTALS REVIEW ###

-- 1. FizzBuzz
PROCEDURE FizzBuzz()
  FOR i FROM 1 TO 100
    IF i MOD 15 == 0 THEN
      PRINT "FizzBuzz"
    ELSE IF i MOD 3 == 0 THEN
      PRINT "Fizz"
    ELSE IF i MOD 5 == 0 THEN
      PRINT "Buzz"
    ELSE
      PRINT i
    END IF
  ENDFOR
END

-- 2. Prime Number Check
FUNCTION isPrime(n AS INTEGER) RETURNS BOOLEAN
  IF n <= 1 THEN
    RETURN false
  END IF
  
  FOR i FROM 2 TO SQRT(n)
    IF n MOD i == 0 THEN
      RETURN false -- Found a factor, so not prime
    END IF
  ENDFOR
  
  RETURN true -- No factors found
END

-- 3. Factorial (Using Recursion)
FUNCTION Factorial(n AS INTEGER) RETURNS INTEGER
  IF n == 0 THEN
    RETURN 1 -- Base case
  ELSE
    RETURN n * Factorial(n - 1) -- Recursive call
  END IF
END

-- 4. Fibonacci Sequence (Using Iteration)
FUNCTION Fibonacci(n AS INTEGER) RETURNS INTEGER
  IF n <= 1 THEN
    RETURN n
  END IF

  DECLARE a = 0, b = 1, temp
  FOR i FROM 2 TO n
    temp = a + b
    a = b
    b = temp
  ENDFOR
  RETURN b
END


-- ### ARRAYS & STRINGS ###

-- 5. Find Maximum Element in an Array
FUNCTION FindMax(arr AS ARRAY OF INTEGER) RETURNS INTEGER
  DECLARE maxVal = arr[0]
  FOR i FROM 1 TO LENGTH(arr) - 1
    IF arr[i] > maxVal THEN
      SET maxVal = arr[i]
    END IF
  ENDFOR
  RETURN maxVal
END

-- 6. Reverse an Array
PROCEDURE ReverseArray(arr AS ARRAY)
  DECLARE start = 0
  DECLARE end = LENGTH(arr) - 1
  WHILE start < end
    -- Swap elements
    DECLARE temp = arr[start]
    SET arr[start] = arr[end]
    SET arr[end] = temp
    
    -- Move pointers
    SET start = start + 1
    SET end = end - 1
  END WHILE
END

-- 7. Check for Palindrome String
FUNCTION isPalindrome(text AS STRING) RETURNS BOOLEAN
  DECLARE left = 0
  DECLARE right = LENGTH(text) - 1
  WHILE left < right
    IF text[left] != text[right] THEN
      RETURN false
    END IF
    SET left = left + 1
    SET right = right - 1
  END WHILE
  RETURN true
END

-- 8. Two Sum Problem
FUNCTION TwoSum(arr AS ARRAY, target AS INTEGER) RETURNS ARRAY
  FOR i FROM 0 TO LENGTH(arr) - 1
    FOR j FROM i + 1 TO LENGTH(arr) - 1
      IF arr[i] + arr[j] == target THEN
        RETURN [i, j] -- Return indices
      END IF
    ENDFOR
  ENDFOR
  RETURN [] -- Return empty array if no solution
END


-- ### SEARCHING & SORTING ALGORITHMS ###

-- 9. Linear Search
FUNCTION LinearSearch(arr AS ARRAY, target) RETURNS INTEGER
  FOR i FROM 0 TO LENGTH(arr) - 1
    IF arr[i] == target THEN
      RETURN i -- Return index if found
    END IF
  ENDFOR
  RETURN -1 -- Return -1 if not found
END

-- 10. Binary Search
FUNCTION BinarySearch(sortedArr AS ARRAY, target) RETURNS INTEGER
  DECLARE left = 0
  DECLARE right = LENGTH(sortedArr) - 1
  
  WHILE left <= right
    DECLARE mid = FLOOR((left + right) / 2)
    IF sortedArr[mid] == target THEN
      RETURN mid
    ELSE IF sortedArr[mid] < target THEN
      SET left = mid + 1
    ELSE
      SET right = mid - 1
    END IF
  END WHILE
  
  RETURN -1 -- Not found
END

-- 11. Bubble Sort
PROCEDURE BubbleSort(arr AS ARRAY)
  DECLARE n = LENGTH(arr)
  FOR i FROM 0 TO n - 2
    FOR j FROM 0 TO n - i - 2
      IF arr[j] > arr[j+1] THEN
        DECLARE temp = arr[j]
        SET arr[j] = arr[j+1]
        SET arr[j+1] = temp
      END IF
    ENDFOR
  ENDFOR
END

-- 12. Selection Sort
PROCEDURE SelectionSort(arr AS ARRAY)
  DECLARE n = LENGTH(arr)
  FOR i FROM 0 TO n - 2
    DECLARE minIndex = i
    FOR j FROM i + 1 TO n - 1
      IF arr[j] < arr[minIndex] THEN
        SET minIndex = j
      END IF
    ENDFOR
    DECLARE temp = arr[minIndex]
    SET arr[minIndex] = arr[i]
    SET arr[i] = temp
  ENDFOR
END


-- ### CORE DATA STRUCTURES ###

-- 13. Linked List: Traversal
DEFINE NODE: { data, next }
PROCEDURE TraverseList(head AS NODE)
  DECLARE current = head
  WHILE current IS NOT NULL
    PRINT current.data
    SET current = current.next
  END WHILE
END

-- 14. Linked List: Insert at End
PROCEDURE InsertAtEnd(head AS NODE, value)
  DECLARE newNode = CREATE_NODE(value)
  IF head IS NULL THEN
    SET head = newNode
    RETURN
  END IF
  
  DECLARE current = head
  WHILE current.next IS NOT NULL
    SET current = current.next
  END WHILE
  SET current.next = newNode
END

-- 15. Stack: Push and Pop
PROCEDURE DemonstrateStack()
  DECLARE stack AS STACK
  PUSH(stack, 10)
  PUSH(stack, 20)
  PRINT POP(stack) -- Prints 20
  PRINT POP(stack) -- Prints 10
END

-- 16. Queue: Enqueue and Dequeue
PROCEDURE DemonstrateQueue()
  DECLARE queue AS QUEUE
  ENQUEUE(queue, "A")
  ENQUEUE(queue, "B")
  PRINT DEQUEUE(queue) -- Prints "A"
  PRINT DEQUEUE(queue) -- Prints "B"
END

-- 17. Stack Application: Balanced Parentheses
FUNCTION isBalanced(expression AS STRING) RETURNS BOOLEAN
  DECLARE stack AS STACK
  FOR EACH char IN expression
    IF char is an opening bracket ('(', '{', '[') THEN
      PUSH(stack, char)
    ELSE IF char is a closing bracket (')', '}', ']') THEN
      IF stack IS EMPTY THEN RETURN false
      DECLARE top = POP(stack)
      IF top does not match char THEN
        RETURN false
      END IF
    END IF
  ENDFOR
  RETURN stack IS EMPTY
END

-- 18. Hash Table (Dictionary): Frequency Count
FUNCTION CountFrequencies(arr AS ARRAY) RETURNS DICTIONARY
  DECLARE freqMap AS DICTIONARY
  FOR EACH item IN arr
    IF item EXISTS IN freqMap THEN
      SET freqMap[item] = freqMap[item] + 1
    ELSE
      SET freqMap[item] = 1
    END IF
  ENDFOR
  RETURN freqMap
END

-- 19. Binary Search Tree (BST): Insertion
DEFINE NODE: { value, left, right }
PROCEDURE InsertIntoBST(node AS NODE, value)
  IF value < node.value THEN
    IF node.left IS NULL THEN
      SET node.left = CREATE_NODE(value)
    ELSE
      InsertIntoBST(node.left, value)
    END IF
  ELSE
    IF node.right IS NULL THEN
      SET node.right = CREATE_NODE(value)
    ELSE
      InsertIntoBST(node.right, value)
    END IF
  END IF
END

-- 20. Binary Tree: In-order Traversal
PROCEDURE InOrderTraversal(node AS NODE)
  IF node IS NOT NULL THEN
    InOrderTraversal(node.left)
    PRINT node.value
    InOrderTraversal(node.right)
  END IF
END

-- 21. Graph: Breadth-First Search (BFS)
PROCEDURE BFS(graph, startNode)
  DECLARE queue AS QUEUE
  DECLARE visited AS SET
  
  ENQUEUE(queue, startNode)
  ADD startNode TO visited
  
  WHILE queue IS NOT EMPTY
    DECLARE currentNode = DEQUEUE(queue)
    PRINT currentNode
    
    FOR EACH neighbor OF currentNode IN graph
      IF neighbor IS NOT IN visited THEN
        ADD neighbor TO visited
        ENQUEUE(queue, neighbor)
      END IF
    ENDFOR
  END WHILE
END

-- 22. Graph: Depth-First Search (DFS)
PROCEDURE DFS(graph, startNode)
  DECLARE stack AS STACK
  DECLARE visited AS SET
  
  PUSH(stack, startNode)
  
  WHILE stack IS NOT EMPTY
    DECLARE currentNode = POP(stack)
    
    IF currentNode IS NOT IN visited THEN
      ADD currentNode TO visited
      PRINT currentNode
      
      FOR EACH neighbor OF currentNode IN graph
        IF neighbor IS NOT IN visited THEN
          PUSH(stack, neighbor)
        END IF
      ENDFOR
    END IF
  END WHILE
END
```
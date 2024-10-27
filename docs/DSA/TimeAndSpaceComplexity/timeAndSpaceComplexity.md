
---

## **Time Complexity**

### 1. **What is Time Complexity?**
   - **Definition**: Time Complexity is a way of analyzing how the execution time of an algorithm increases with the input size (denoted as \(n\)).
   - **Goal**: To understand and compare the efficiency of algorithms, especially as input sizes grow.

### 2. **Common Time Complexity Notations**
   - **Big-O Notation \(O(f(n))\)**: Describes the **upper bound** of the algorithm’s runtime, focusing on the worst-case scenario.
   - **Theta Notation \(\Theta(f(n))\)**: Describes the **tight bound** of runtime, focusing on the average case.
   - **Omega Notation \(\Omega(f(n))\)**: Describes the **lower bound** of runtime, focusing on the best-case scenario.

### 3. **Common Time Complexities**

| Complexity     | Notation         | Example                                |
|----------------|------------------|----------------------------------------|
| Constant       | \(O(1)\)         | Accessing an element in an array       |
| Logarithmic    | \(O(\log n)\)    | Binary Search                          |
| Linear         | \(O(n)\)         | Linear Search                          |
| Linearithmic   | \(O(n \log n)\)  | Merge Sort, Quick Sort                 |
| Quadratic      | \(O(n^2)\)       | Bubble Sort, Selection Sort            |
| Cubic          | \(O(n^3)\)       | 3 nested loops                         |
| Exponential    | \(O(2^n)\)       | Recursive Fibonacci                    |
| Factorial      | \(O(n!)\)        | Generating all permutations            |

### 4. **How to Calculate Time Complexity**

   - **Loops**: Analyze how many times a loop runs.
     - Example: 
       ```python
       for i in range(n):     # Runs O(n) times
           print(i)
       ```
   - **Nested Loops**: Multiply the time complexity of each loop.
     - Example:
       ```python
       for i in range(n):          # O(n)
           for j in range(n):      # O(n)
               print(i, j)         # O(1)
       ```
       *Total Complexity*: \(O(n) \times O(n) = O(n^2)\).
   - **Recursive Functions**: Use recurrence relations to calculate the complexity. For example, `T(n) = T(n-1) + O(1)` results in \(O(n)\).
   
### 5. **Common Mistakes in Time Complexity Calculations**
   - **Ignoring inner operations**: Remember that nested operations increase complexity (e.g., two nested loops are \(O(n^2)\), not \(O(n)\)).
   - **Not simplifying correctly**: Only the highest-order term matters (e.g., \(O(n + n^2) \rightarrow O(n^2)\)).
   - **Ignoring logarithmic operations**: Be cautious with algorithms that halve the input (like Binary Search, which is \(O(\log n)\)).

---

## **Space Complexity**

### 1. **What is Space Complexity?**
   - **Definition**: Space Complexity measures the amount of memory an algorithm needs to run, based on input size \(n\).
   - **Goal**: Minimize the memory usage of your code, especially for large input sizes.

### 2. **Types of Space Complexity**

   - **Auxiliary Space**: The extra space or temporary space used by the algorithm, excluding input size.
   - **Total Space**: The sum of input size and auxiliary space used by the algorithm.

### 3. **Common Space Complexities**

| Complexity     | Notation         | Example                                 |
|----------------|------------------|-----------------------------------------|
| Constant       | \(O(1)\)         | Using a fixed number of variables       |
| Linear         | \(O(n)\)         | Storing data in an array                |
| Quadratic      | \(O(n^2)\)       | Using a 2D matrix for dynamic programming|
| Logarithmic    | \(O(\log n)\)    | Storing recursive calls in binary search|

### 4. **How to Calculate Space Complexity**

   - **Primitive Variables**: Each primitive (e.g., `int`, `char`) requires constant space \(O(1)\).
     - Example:
       ```python
       a = 10       # O(1)
       b = [1, 2, 3] # O(n), where n is the number of elements in the list
       ```
   - **Data Structures**: Space depends on the data structure's size.
     - List of \(n\) elements → \(O(n)\)
     - 2D array of \(n \times n\) → \(O(n^2)\)
   - **Recursive Functions**: Each recursive call adds a new frame to the call stack.
     - Recursive depth of \(n\) (linear recursion) → \(O(n)\)
     - Binary recursion with depth of \(\log n\) → \(O(\log n)\)

### 5. **Common Mistakes in Space Complexity Calculations**
   - **Overlooking function calls in recursion**: Each recursive call adds to the call stack.
   - **Miscounting data structure space**: Remember to account for auxiliary space (temporary arrays, lists).
   - **Ignoring constants in auxiliary variables**: Multiple variables don't change linear complexity, but they do matter if additional lists or arrays grow with \(n\).

---

## **Examples and Patterns for Time and Space Complexity**

### 1. **Example: Linear Time Complexity \(O(n)\)**
   - Problem: Summing elements in an array.
   - Solution:
     ```python
     def sum_array(arr):
         total = 0
         for num in arr:
             total += num
         return total
     ```
     **Time Complexity**: \(O(n)\) – iterates through each element once.
     **Space Complexity**: \(O(1)\) – only a few variables used.

### 2. **Example: Quadratic Time Complexity \(O(n^2)\)**
   - Problem: Checking for duplicate pairs in an array.
   - Solution:
     ```python
     def check_duplicates(arr):
         for i in range(len(arr)):
             for j in range(i + 1, len(arr)):
                 if arr[i] == arr[j]:
                     return True
         return False
     ```
     **Time Complexity**: \(O(n^2)\) – double loop iterates over each pair.
     **Space Complexity**: \(O(1)\) – no extra data structure used.

### 3. **Example: Recursive Complexity \(O(2^n)\)**
   - Problem: Calculating Fibonacci sequence.
   - Solution:
     ```python
     def fibonacci(n):
         if n <= 1:
             return n
         return fibonacci(n - 1) + fibonacci(n - 2)
     ```
     **Time Complexity**: \(O(2^n)\) – each call splits into two more calls.
     **Space Complexity**: \(O(n)\) – due to call stack depth of \(n\).


---

# Implementation with examples 


### 1. O(1) - Constant Time
- **Definition**: The algorithm takes the same amount of time regardless of the input size.
- **Characteristics**: No loops or recursion. A fixed number of operations.
- **Examples**:
  - Accessing an element in an array by index.
  - Performing basic arithmetic operations.

  ```python
  def get_first_element(arr):
      return arr[0]  # O(1)
  ```

### 2. O(n) - Linear Time
- **Definition**: The algorithm’s time grows linearly with the input size.
- **Characteristics**: A single loop that runs `n` times, where `n` is the size of the input.
- **Examples**:
  - Iterating through all elements in an array.

  ```python
  def find_element(arr, target):
      for elem in arr:
          if elem == target:
              return True
      return False  # O(n)
  ```

### 3. O(n^2) - Quadratic Time
- **Definition**: The algorithm’s time grows quadratically with the input size.
- **Characteristics**: Nested loops, each running `n` times.
- **Examples**:
  - Comparing each element with every other element (e.g., bubble sort).

  ```python
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n):
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]  # O(n^2)
  ```

### 4. O(log n) - Logarithmic Time
- **Definition**: The algorithm’s time grows logarithmically as the input size increases.
- **Characteristics**: The problem size is reduced by a constant fraction (usually by half) each time.
- **Examples**:
  - Binary search in a sorted array.

  ```python
  def binary_search(arr, target):
      left, right = 0, len(arr) - 1
      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return True
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
      return False  # O(log n)
  ```

### 5. O(n log n) - Linearithmic Time
- **Definition**: The algorithm’s time is a combination of linear and logarithmic growth.
- **Characteristics**: Divide-and-conquer algorithms, often seen in efficient sorting algorithms.
- **Examples**:
  - Merge sort, quick sort (average case).

  ```python
  def merge_sort(arr):
      if len(arr) > 1:
          mid = len(arr) // 2
          left_half = arr[:mid]
          right_half = arr[mid:]

          merge_sort(left_half)
          merge_sort(right_half)

          i = j = k = 0

          while i < len(left_half) and j < len(right_half):
              if left_half[i] < right_half[j]:
                  arr[k] = left_half[i]
                  i += 1
              else:
                  arr[k] = right_half[j]
                  j += 1
              k += 1

          while i < len(left_half):
              arr[k] = left_half[i]
              i += 1
              k += 1

          while j < len(right_half):
              arr[k] = right_half[j]
              j += 1
              k += 1  # O(n log n)
  ```

### How to Determine Complexity

#### 1. **Identify Basic Operations**
   - What are the core operations (comparisons, arithmetic, etc.)?

#### 2. **Analyze Loops**
   - **Single Loop**: Typically O(n).
   - **Nested Loops**: Typically O(n^2), O(n^3), etc., depending on the depth.

   ```python
   def example_single_loop(arr):
       for i in range(len(arr)):
           print(arr[i])  # O(n)

   def example_nested_loop(arr):
       for i in range(len(arr)):
           for j in range(len(arr)):
               print(arr[i] + arr[j])  # O(n^2)
   ```

#### 3. **Analyze Recursive Calls**
   - How many times does the function call itself, and how does the input size change?

   ```python
   def fib(n):
       if n <= 1:
           return n
       return fib(n-1) + fib(n-2)  # O(2^n)
   ```

#### 4. **Consider Problem Reduction**
   - Does the problem size get reduced by half or a constant fraction each step?

   ```python
   def binary_search(arr, target):
       left, right = 0, len(arr) - 1
       while left <= right:
           mid = (left + right) // 2
           if arr[mid] == target:
               return True
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       return False  # O(log n)
   ```

#### 5. **Combine and Simplify**
   - Combine the complexities from different parts of the code and simplify using Big O notation (drop constants and non-dominant terms).

### Practical Examples

#### Example 1: Iterating Over an Array

```python
def print_all_elements(arr):
    for elem in arr:
        print(elem)  # O(n) because it iterates over each element once.
```

#### Example 2: Checking Pairs in an Array

```python
def check_pairs(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(arr[i], arr[j])  # O(n^2) because of the nested loops.
```




#### Example 3: Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False  # O(log n) because the search space is halved each iteration.
```

By following these steps and examples, you can determine whether an algorithm is O(1), O(n), O(n^2), O(log n), or any other complexity. Understanding the structure and behavior of the algorithm, particularly how it handles input and how many operations it performs, is key to analyzing its complexity.







Space complexity analysis is somewhat similar to time complexity analysis but focuses on the amount of memory an algorithm uses as a function of the input size. Here’s a detailed guide on how to determine space complexity with explanations and examples.

### Understanding Space Complexity

#### Step-by-Step Process

1. **Identify Extra Variables**: Look at the variables and data structures that require extra memory.
2. **Analyze Recursion**: Consider the additional stack space used by recursive calls.
3. **Account for Data Structures**: Include the memory required for data structures like arrays, lists, hash tables, etc.
4. **Ignore Input Size**: Space used by the input itself is usually not counted.

### 1. O(1) - Constant Space
- **Definition**: The algorithm uses a fixed amount of extra memory regardless of the input size.
- **Characteristics**: Uses only a few variables.
- **Examples**:
  - Simple variable assignments and arithmetic operations.

  ```python
  def get_first_element(arr):
      return arr[0]  # O(1) space because it uses only one variable.
  ```

### 2. O(n) - Linear Space
- **Definition**: The algorithm’s memory usage grows linearly with the input size.
- **Characteristics**: Uses data structures like arrays or lists that scale with the input.
- **Examples**:
  - Creating a new list of size `n`.

  ```python
  def create_list(n):
      new_list = [0] * n  # O(n) space because the list size depends on n.
      return new_list
  ```

### 3. O(n^2) - Quadratic Space
- **Definition**: The algorithm’s memory usage grows quadratically with the input size.
- **Characteristics**: Typically seen with 2D arrays or matrices.
- **Examples**:
  - Creating a 2D matrix of size `n x n`.

  ```python
  def create_matrix(n):
      matrix = [[0] * n for _ in range(n)]  # O(n^2) space because of the 2D matrix.
      return matrix
  ```

### 4. Recursive Algorithms
- **Definition**: Consider the stack space required by recursive calls.
- **Characteristics**: Each recursive call adds a new frame to the stack.
- **Examples**:
  - Calculating the factorial of a number.

  ```python
  def factorial(n):
      if n == 0:
          return 1
      return n * factorial(n - 1)  # O(n) space because of the recursion stack.
  ```

### Practical Examples

#### Example 1: Iterating Over an Array (O(1) Space)

```python
def print_all_elements(arr):
    for elem in arr:
        print(elem)  # O(1) space because no extra memory is used.
```

#### Example 2: Creating a New List (O(n) Space)

```python
def double_elements(arr):
    result = []
    for elem in arr:
        result.append(elem * 2)  # O(n) space because the new list's size depends on the input.
    return result
```

#### Example 3: Merge Sort (O(n) Space)

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]  # O(n/2)
        right_half = arr[mid:]  # O(n/2)

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1  # O(n) space due to auxiliary arrays.
```

### Detailed Analysis of Space Complexity

#### Example: Iterative Algorithm with a Single Loop

```python
def sum_elements(arr):
    total = 0
    for elem in arr:
        total += elem  # O(1) space because only a single integer variable is used.
    return total
```

- **Extra Variables**: Only `total` is used.
- **Space Complexity**: O(1)

#### Example: Algorithm with Additional Data Structures

```python
def copy_elements(arr):
    new_arr = []
    for elem in arr:
        new_arr.append(elem)  # O(n) space because a new array of the same size is created.
    return new_arr
```

- **Extra Variables**: `new_arr` which scales with the input size.
- **Space Complexity**: O(n)

#### Example: Recursive Algorithm

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(n) space because of the recursion stack.
```

- **Extra Variables**: Stack frames for each recursive call.
- **Space Complexity**: O(n) due to the depth of the recursion stack.

### Combining Multiple Factors

Sometimes, algorithms involve multiple steps with different space complexities. In such cases, analyze each part and then combine them.

#### Example: Recursive Algorithm with Helper Function

```python
def helper(arr, n):
    if n == 0:
        return []
    return helper(arr, n-1) + [arr[n-1]]  # O(n) space due to recursion and list concatenation.

def reverse_list(arr):
    return helper(arr, len(arr))
```

- **Helper Function Space**: O(n) due to recursion depth and list concatenation.
- **Total Space Complexity**: O(n)

### Practical Tips

1. **Count Extra Variables**: Identify how many variables, data structures, and their sizes.
2. **Analyze Recursive Calls**: Consider the maximum depth of the recursion stack.
3. **Include Data Structures**: Account for arrays, lists, dictionaries, etc., that scale with input size.
4. **Combine Results**: For multiple steps, analyze each and combine the space requirements.

By understanding these principles and analyzing algorithms with a structured approach, you can determine the space complexity accurately.
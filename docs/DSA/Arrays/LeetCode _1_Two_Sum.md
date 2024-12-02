### **Interview Simulation: LeetCode 1 - Two Sum**

---

**Interviewer**:  
Let’s solve another common problem. You’re given an array of integers `nums` and an integer `target`. Return the indices of the two numbers in the array that add up to the `target`. Assume each input would have exactly one solution, and you may not use the same element twice.

---

### **Step 1: Understanding the Problem**

**Candidate**:  
Let me confirm my understanding:  
- I need to find two numbers in the array whose sum equals the `target`.  
- I should return the indices of these two numbers, not the numbers themselves.  
- Each input is guaranteed to have exactly one solution, so I don’t need to handle cases with no solution or multiple solutions.  
Is that correct?  

**Interviewer**:  
Yes, that’s correct. How would you approach this?

---

### **Step 2: Brute Force Solution**

**Candidate**:  
To start with the simplest approach, I can use a nested loop:  
1. For each number in the array, I’ll iterate through the rest of the array to find a pair that sums to the `target`.  
2. When I find such a pair, I’ll return their indices.  

Here’s the code:  

```python
def twoSum(nums, target):
    for i in range(len(nums)):  # Loop through each element
        for j in range(i + 1, len(nums)):  # Compare with elements after it
            if nums[i] + nums[j] == target:  # Check if they sum to target
                return [i, j]  # Return the indices
```

**Interviewer**:  
What’s the time and space complexity of this solution?  

**Candidate**:  
- **Time Complexity**: O(n²) because of the nested loops.  
- **Space Complexity**: O(1) since we’re not using any extra space.  

**Interviewer**:  
Good. Is there a more efficient way to solve this?  

---

### **Step 3: Optimized Solution (HashMap)**

**Candidate**:  
Yes, I can optimize this using a HashMap:  
1. As I iterate through the array, I’ll calculate the complement for each number, which is `target - nums[i]`.  
2. I’ll check if the complement already exists in the HashMap.  
3. If it exists, I’ve found the pair, and I’ll return their indices.  
4. Otherwise, I’ll store the current number and its index in the HashMap for future lookups.  

Here’s the code:  

```python
def twoSum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):  # Loop through the array
        complement = target - num  # Calculate the complement
        if complement in num_map:  # Check if complement is already in the dictionary
            return [num_map[complement], i]  # Return the indices
        num_map[num] = i  # Store the current number and its index in the dictionary
```

**Interviewer**:  
Great! What’s the time and space complexity of this approach?  

**Candidate**:  
- **Time Complexity**: O(n), because we iterate through the array once, and dictionary lookups take O(1) on average.  
- **Space Complexity**: O(n), as we store up to `n` elements in the dictionary.  

---

### **Step 4: Edge Cases**

**Interviewer**:  
What edge cases would you consider for this problem?  

**Candidate**:  
Here are some edge cases:  
1. **Negative numbers**: Ensure the solution works when `nums` contains negative numbers.  
   - Example: `nums = [-1, -2, -3, -4], target = -6` -> `True`.  
2. **Zero in the array**: The complement could be `0`.  
   - Example: `nums = [0, 4, 3, 0], target = 0` -> `True`.  
3. **Large inputs**: Test the solution with a large array to ensure it’s efficient.  

---

### **Step 5: Explaining HashMap Logic**

**Interviewer**:  
Can you explain why the HashMap approach is more efficient than brute force?  

**Candidate**:  
Of course!  
- In the brute force solution, we compare every pair of elements, leading to O(n²) time complexity.  
- The HashMap approach avoids unnecessary comparisons by using quick lookups:  
  - When iterating, we calculate the complement and immediately check if it’s in the HashMap.  
  - This reduces the complexity to O(n), as we only traverse the array once and perform constant-time lookups.  

---

### **Step 6: Alternative Approach (Sorting + Two Pointers)**

**Interviewer**:  
Can you solve this problem without using extra space?  

**Candidate**:  
Yes, I can use a sorting + two-pointer approach:  
1. I’ll sort the array, then use two pointers—one at the beginning and one at the end.  
2. I’ll calculate the sum of the elements at the two pointers:  
   - If the sum is equal to `target`, return the indices.  
   - If the sum is less than `target`, move the left pointer to the right.  
   - If the sum is greater than `target`, move the right pointer to the left.  

However, sorting changes the order of the indices, so I’d need to track the original indices separately.  

Here’s the code:  

```python
def twoSum(nums, target):
    nums_with_index = [(num, i) for i, num in enumerate(nums)]  # Pair numbers with indices
    nums_with_index.sort()  # Sort by numbers
    left, right = 0, len(nums_with_index) - 1

    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]  # Sum of two pointers
        if current_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]  # Return original indices
        elif current_sum < target:
            left += 1  # Move left pointer to the right
        else:
            right -= 1  # Move right pointer to the left
```

**Interviewer**:  
What’s the complexity here?  

**Candidate**:  
- **Time Complexity**: O(n log n) due to sorting.  
- **Space Complexity**: O(n), as we store the array with indices.  

---

### **Step 7: Summary**

**Interviewer**:  
Can you summarize your approaches?  

**Candidate**:  
Sure!  
1. **Problem**: Find two indices in an array whose values sum to a given target.  
2. **Brute Force**: Use nested loops to check all pairs (O(n²), O(1)).  
3. **Optimized**: Use a HashMap to store complements and indices (O(n), O(n)).  
4. **Alternative**: Sort the array and use two pointers (O(n log n), O(n)).  
5. **Edge Cases**: Negative numbers, zeros, large inputs.  

---

### **Flashcard for Revision**

**Problem**: LeetCode 1 - Two Sum  
**Tags**: Hashing, Two Pointers, Arrays  
**Approaches**:  
- **Brute Force**: Compare all pairs (O(n²), O(1)).  
- **Optimized (HashMap)**: Store complements and indices (O(n), O(n)).  
- **Two Pointers**: Sort and use two pointers (O(n log n), O(n)).  
**Key Points**:  
- HashMap approach is the most efficient.  
- Sorting + two-pointer works but requires extra space to track indices.  
**Edge Cases**: Negative numbers, zeros, large inputs.  

---

How does this feel? Ready for the next problem? 😊
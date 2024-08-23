# Remove Duplicates from Sorted Array

## Problem Description

**Objective:**  
Remove duplicates from a sorted integer array `nums` in-place such that each element appears only once, and return the new length of the array.

**Constraints:**
- The array `nums` is sorted in non-decreasing order.
- The solution must be performed in-place with no extra space.

**Example:**

- **Input:** `nums = [1, 1, 2]`  
  **Output:** `2, nums = [1, 2, _]`

- **Input:** `nums = [0, 0, 1, 1, 2, 2, 3]`  
  **Output:** `4, nums = [0, 1, 2, 3, _, _, _]`

## Approach

1. **Initial Setup:**  
   Return `0` if the array `nums` is empty.

2. **Iterate and Place Unique Elements:**  
   Use a pointer `k` to track the position for the next unique element. Start with `k = 1`. Compare each element with the previous one; if different, place it at `k` and increment `k`.

3. **Return Result:**  
   Return `k` which is the count of unique elements in the array.

## Solution

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 1  # Pointer for placing unique elements
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

Class `Solution` with method `removeDuplicates` takes a list of integers `nums` and performs the following:

- Checks if `nums` is empty and returns `0` if true.
- Initializes a pointer `k` to `1`.
- Iterates through the list starting from the second element. For each element, if it is different from the previous element, assigns it to `nums[k]` and increments `k`.
- Returns the value of `k`, which represents the number of unique elements in the array.

### Explanation
- **Initialization:** Checks if the array is empty and returns `0`.
- **Unique Element Placement:** Starts placing unique elements from index `1`.
- **Iteration:** Compares each element with its predecessor. If they differ, updates position `k`.
- **Return Length:** Returns the count of unique elements.

### Complexity Analysis
- **Time Complexity:** O(n), where `n` is the number of elements in the array.
- **Space Complexity:** O(1), as modifications are done in-place.

## How to Use This Repository

1. **Clone the Repository:**  
   `git clone https://github.com/superALLEY/150InterviewQuestions.git`

2. **Navigate to the Problem Folder:**  
   Locate the "Remove Duplicates" problem folder.

3. **Run the Solution:**  
   Open the solution file in your IDE and execute it to test various cases.

## Contributing

1. **Fork the Repository.**
2. **Create a New Branch:**  
   `git checkout -b feature/problem-name`

3. **Commit Your Changes:**  
   `git commit -am 'Add problem-name solution'`

4. **Push to the Branch:**  
   `git push origin feature/problem-name`

5. **Create a Pull Request.**

## License

This repository is licensed under the MIT License. You are free to use the code for learning and interview preparation.

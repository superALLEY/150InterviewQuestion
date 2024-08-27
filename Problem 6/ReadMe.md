
# Array Rotation

## Problem Description

**Objective:**  
Given an array `nums` of size `n`, rotate the array to the right by `k` steps, where `k` is a non-negative integer. The rotation should be done in-place.

**Constraints:**
- The array should be rotated in-place with O(1) extra space.
- The algorithm should run in linear time, `O(n)`.

**Example:**

- **Input:** `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`  
  **Output:** `[5, 6, 7, 1, 2, 3, 4]`  
  **Explanation:** The array is rotated to the right by 3 steps.

- **Input:** `nums = [-1, -100, 3, 99]`, `k = 2`  
  **Output:** `[3, 99, -1, -100]`  
  **Explanation:** The array is rotated to the right by 2 steps.

## Approach

### Reversal Method

This problem is efficiently solved using the **Reversal Method**. The algorithm involves reversing parts of the array to achieve the rotation in-place.

1. **Reverse the Entire Array:**  
   - First, reverse the entire array. This will move the elements that need to be rotated to the front to the back, and vice versa.

2. **Reverse the First `k` Elements:**  
   - Next, reverse the first `k` elements. This reorders the first part of the array.

3. **Reverse the Remaining Elements:**  
   - Finally, reverse the rest of the array (from index `k` to the end). This places the remaining elements in the correct order.

   ```python
   class Solution(object):
       def rotate(self, nums, k):
           n = len(nums)
           k = k % n  # In case k is greater than n

           # Step 1: Reverse the entire array
           self.reverse(nums, 0, n - 1)
           # Step 2: Reverse the first k elements
           self.reverse(nums, 0, k - 1)
           # Step 3: Reverse the rest of the array
           self.reverse(nums, k, n - 1)

       def reverse(self, nums, start, end):
           while start < end:
               nums[start], nums[end] = nums[end], nums[start]
               start += 1
               end -= 1
   ```

### Example Walkthrough with `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`:

- **Initialization:**  
  Reverse the entire array: `[7, 6, 5, 4, 3, 2, 1]`.

- **Reverse the First 3 Elements:**
  - After reversing: `[5, 6, 7, 4, 3, 2, 1]`.

- **Reverse the Remaining Elements:**
  - After reversing: `[5, 6, 7, 1, 2, 3, 4]`.

- **Final Output:**  
  The algorithm returns `[5, 6, 7, 1, 2, 3, 4]`.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the number of elements in the array. The algorithm iterates through the array a constant number of times.
- **Space Complexity:** `O(1)` since the reversal is done in-place with no extra space.

## How to Use This Repository

1. **Clone the Repository:**  
   `git clone https://github.com/superALLEY/150InterviewQuestions.git`

2. **Navigate to the Problem Folder:**  
   Locate the folder for the "Array Rotation" problem.

3. **Run the Solution:**  
   Open the solution file in your preferred IDE and execute it to see the results.

## Contributing

Contributions are always welcome! To contribute:

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

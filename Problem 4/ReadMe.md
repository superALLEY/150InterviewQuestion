# Remove Duplicates from Sorted Array (Allowing at Most Two Occurrences)

## Problem Description

**Objective:**  
Given a sorted integer array `nums`, remove the duplicates in-place such that each element appears at most twice. The relative order of the elements should be maintained. The function should return the new length of the array after removing the extra duplicates.

**Constraints:**
- The input array `nums` will be sorted in non-decreasing order.
- The operation should be performed in-place without using extra space.

**Example:**

- **Input:** `nums = [1, 1, 1, 2, 2, 3]`  
  **Output:** `5, nums = [1, 1, 2, 2, 3]`  
  **Explanation:** The function returns `5`, with the first five elements of `nums` being `1`, `1`, `2`, `2`, `3`. The remaining elements can be ignored.

## Approach

1. **Initial Setup:**  
   - Initialize a pointer `k` to `1`, which will be used to place the next allowed element.
   - Initialize a counter `c` to `1`, which will track the number of occurrences of the current element.

2. **Iterating Over the Array:**  
   - Use a `while` loop starting from the second element (`i = 1`) and iterate through the array.
   - For each element, compare it with the previous element:
     - If it is different, place it at position `k`, increment `k`, and reset `c` to `1`.
     - If it is the same and `c < 2`, place it at position `k`, increment both `k` and `c`.
     - If it is the same and `c >= 2`, skip the element.

3. **Return Result:**  
   - After completing the iteration, return `k`, which is the new length of the array with duplicates removed or reduced to at most two occurrences.

## Solution Code

```python
class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        c = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
                c = 1
            elif c < 2 and nums[i] == nums[i-1]:
                nums[k] = nums[i]
                k += 1
                c += 1
            i += 1
        return k

        
```
## Explanation

- **Initialization:**  
  The pointer `k` starts at `1` to place unique or allowed duplicate elements. The counter `c` tracks how many times the current element has been encountered.

- **Iteration:**  
  The loop iterates over the array starting from the second element. If an element is different from its predecessor, it is placed in the position pointed to by `k`. If it is the same but allowed (less than twice), it is also placed.

- **Final Output:**  
  The method returns the value of `k`, which represents the number of valid elements in the array after processing.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the number of elements in the array. The method iterates through the array once.
- **Space Complexity:** `O(1)` as the operation is performed in-place without extra space.

## How to Use This Repository

1. **Clone the Repository:**  
   `git clone https://github.com/superALLEY/150InterviewQuestions.git`

2. **Navigate to the Problem Folder:**  
   Locate the folder for the "Remove Duplicates" problem.

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


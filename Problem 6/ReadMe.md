
# Majority Element

## Problem Description

**Objective:**  
Given an array `nums` of size `n`, the task is to find the majority element. The majority element is the element that appears more than `n/2` times in the array.

**Constraints:**
- The input array `nums` will always have a majority element, meaning an element that appears more than `n/2` times.
- The algorithm should run in linear time, `O(n)`, and use `O(1)` extra space.

**Example:**

- **Input:** `nums = [3, 2, 3]`  
  **Output:** `3`  
  **Explanation:** The majority element `3` appears twice in the array of size 3.

- **Input:** `nums = [2, 2, 1, 1, 1, 2, 2]`  
  **Output:** `2`  
  **Explanation:** The majority element `2` appears four times in the array of size 7.

## Approach

### Boyer-Moore Voting Algorithm

This problem is efficiently solved using the **Boyer-Moore Voting Algorithm**. The algorithm works by maintaining a candidate for the majority element and a counter. The counter is used to track the balance between the candidate and other elements.

1. **Initialization:**  
   - Start with `count = 0` and `candidate = None`.

2. **Iteration:**
   - Iterate through each element in the array `nums`.
   - If `count` is `0`, update the `candidate` to the current element.
   - If the current element matches the `candidate`, increment `count` by `1`.
   - If the current element does not match the `candidate`, decrement `count` by `1`.

3. **Result:**  
   - After completing the iteration, the `candidate` will be the majority element.

   ```python
   class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

   ```

### Example Walkthrough with `nums = [4, 4, 5, 5, 5, 4, 5, 5, 5, 5]`:

- **Initialization:**  
  Start with `count = 0` and `candidate = None`.

- **Iteration:**
  - First element `4`: Since `count` is `0`, `candidate` is set to `4`, `count` is incremented to `1`.
  - Second element `4`: It matches the `candidate`, so `count` is incremented to `2`.
  - Third element `5`: It doesn't match the `candidate`, so `count` is decremented to `1`.
  - Fourth element `5`: It doesn't match the `candidate`, so `count` is decremented to `0`.
  - Fifth element `5`: Since `count` is `0`, `candidate` is set to `5`, `count` is incremented to `1`.
  - Sixth element `4`: It doesn't match the `candidate`, so `count` is decremented to `0`.
  - Seventh element `5`: Since `count` is `0`, `candidate` is set to `5`, `count` is incremented to `1`.
  - Eighth element `5`: It matches the `candidate`, so `count` is incremented to `2`.
  - Ninth element `5`: It matches the `candidate`, so `count` is incremented to `3`.
  - Tenth element `5`: It matches the `candidate`, so `count` is incremented to `4`.

- **Final Output:**  
  The algorithm returns `5` as the majority element.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the number of elements in the array. The algorithm iterates through the array once.
- **Space Complexity:** `O(1)` since only a few extra variables are used.

## How to Use This Repository

1. **Clone the Repository:**  
   `git clone https://github.com/superALLEY/150InterviewQuestions.git`

2. **Navigate to the Problem Folder:**  
   Locate the folder for the "Majority Element" problem.

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

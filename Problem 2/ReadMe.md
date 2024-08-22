# Remove Element

**Difficulty**: Easy

## Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place and return the new length of the array.

The relative order of the elements may be changed. It doesn't matter what you leave beyond the returned length.

### Constraints
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

### Example 1

Input:  
nums = [3, 2, 2, 3]  
val = 3  

Output:  
2, nums = [2, 2, _, _]  

Explanation:  
Your function should return k = 2, with the first two elements of `nums` being 2. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Example 2

Input:  
nums = [0, 1, 2, 2, 3, 0, 4, 2]  
val = 2  

Output:  
5, nums = [0, 1, 4, 0, 3, _, _, _]  

Explanation:  
Your function should return k = 5, with the first five elements of `nums` containing 0, 1, 4, 0, and 3. The order of those five elements can be arbitrary. It does not matter what you leave beyond the returned `k` (hence they are underscores).

## Approach

**Initial Setup:**  
Use a pointer `k` to keep track of the position of elements that should remain in the array after removing all occurrences of `val`.

**Iterating Over the Array:**  
Iterate through the array using a loop. For each element, if it is not equal to `val`, assign it to the position `k` and increment `k`.

**Final Steps:**  
After completing the loop, `k` will contain the new length of the array with all `val` elements removed. The array will have all valid elements at the beginning, and the rest can be ignored or replaced.

## Solution

Class Solution:
    def removeElement(self, nums, val):
        k = 0  # Initialize the counter for the new length
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k  # Return the new length of the array

## Explanation

The loop goes through each element of the array. If the element is not equal to `val`, it is placed at the position indicated by `k`, and `k` is incremented. This method efficiently removes all occurrences of `val` without requiring additional space. The function returns the new length of the array, which is `k`.

## Complexity Analysis

**Time Complexity:** O(n), where `n` is the number of elements in the array.  
**Space Complexity:** O(1), since we are modifying the array in-place without using extra space.

## Additional Notes

This problem tests your ability to modify an array in-place and handle edge cases such as an empty array or an array where all elements are equal to `val`. The problem is common in interviews as it checks both logical thinking and familiarity with array manipulation techniques.

## Contribution

If you have suggestions or improvements, feel free to create a pull request. Contributions are welcome!

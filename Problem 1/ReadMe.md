# Merge Sorted Array

**Difficulty**: Easy

## Problem Description

You are given two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order. Additionally, you are given two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. 

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

### Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

### Example 1

**Input**:
```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Output:

python
Copier le code
[1, 2, 2, 3, 5, 6]
Explanation:
The arrays we are merging are [1, 2, 3] and [2, 5, 6]. The result of the merge is [1, 2, 2, 3, 5, 6] with the underlined elements coming from nums1.

Example 2
Input:

python
Copier le code
nums1 = [1]
m = 1
nums2 = []
n = 0
Output:

python
Copier le code
[1]
Explanation:
The arrays we are merging are [1] and []. The result of the merge is [1].

Example 3
Input:

python
Copier le code
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Output:

python
Copier le code
[1]
Explanation:
The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Approach
Initial Setup:

Use two pointers, i and j, to traverse nums1 and nums2 from the end towards the beginning.
Use another pointer k to track the position in nums1 where the next largest element should be placed.
Merge Process:

Compare elements from the end of nums1 and nums2 and place the larger element in the correct position in nums1.
Decrement the respective pointers accordingly.
Handle Remaining Elements:

If there are any remaining elements in nums2, place them in nums1.
Solution
python
Copier le code
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        i, j, k = m - 1, n - 1, m + n - 1
        
        # Merge nums1 and nums2 from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
Explanation
The pointers i and j start at the end of nums1 and nums2, respectively. k starts at the end of the merged array.
Compare the elements pointed to by i and j, and place the larger one in the position k.
If nums2 still has elements after nums1 is exhausted, they are copied to the beginning of nums1.
Complexity Analysis
Time Complexity: O(m + n), where m and n are the number of elements in nums1 and nums2, respectively. This is because each element is processed exactly once.
Space Complexity: O(1), as the merge is done in-place without extra space.
Additional Notes
This problem tests your ability to merge two sorted arrays efficiently and handle in-place modifications.
A follow-up challenge is to implement an algorithm that runs in O(m + n) time, which is addressed in the above approach.
Coding Interview Preparation
Practicing merging and sorting problems helps in developing efficient algorithmic skills, which are crucial for technical interviews.

Related Problems
Merge Intervals
Sort Colors
Find the Median from Data Stream
Contribution
If you have suggestions or improvements, feel free to create a pull request. Contributions are welcome!
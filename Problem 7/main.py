class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # After the loop, k will be the new length of the array without the `val` elements
        # Optionally, truncate the list to the new length if required
        nums[:] = nums[:k]

        return k  # Return the new length of the array

# Example usage:
sol = Solution()
nums = [3, 2, 2, 3]
val = 3
new_length = sol.removeElement(nums, val)
print("New length:", new_length)  # Output: New length: 2
print("Modified list:", nums)  # Output: Modified list: [2, 2]

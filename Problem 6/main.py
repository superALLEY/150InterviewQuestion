class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
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

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)
print(nums)  # Expected output: [5, 6, 7, 1, 2, 3, 4]

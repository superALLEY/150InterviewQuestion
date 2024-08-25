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

nums = [4, 4, 5, 5, 5, 4, 5, 5, 5, 5]

solution = Solution()
result = solution.majorityElement(nums)
print(result)


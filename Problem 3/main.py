class Solution:
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted list `nums` in-place.
        
        :param nums: List[int] - A sorted list of integers
        :return: int - The length of the list after duplicates have been removed
        """
        if not nums:
            return 0
        
        k = 1  # Pointer for placing unique elements
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

def main():
    # Example usage of the Solution class
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 2]
    length1 = solution.removeDuplicates(nums1)
    print(f"New length: {length1}, Modified list: {nums1[:length1]}")

    # Test case 2
    nums2 = [0, 0, 1, 1, 2, 2, 3]
    length2 = solution.removeDuplicates(nums2)
    print(f"New length: {length2}, Modified list: {nums2[:length2]}")

if __name__ == "__main__":
    main()

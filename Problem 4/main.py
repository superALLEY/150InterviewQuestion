class Solution(object):
    def removeDuplicates(self, nums):
        k = 1  # Pointer to place the next unique element or allowed duplicate
        c = 1  # Counter to track occurrences of the current element
        i = 1  # Start from the second element
        
        while i < len(nums):  # Iterate over the array
            if nums[i] != nums[i - 1]:  # If current element is different from the previous one
                nums[k] = nums[i]  # Place it in the k-th position
                k += 1  # Increment the pointer
                c = 1  # Reset the counter since it's a new element
            elif c < 2:  # If the element is the same but hasn't appeared twice yet
                nums[k] = nums[i]  # Allow it to be placed
                k += 1  # Increment the pointer
                c += 1  # Increment the counter for this element
            
            i += 1  # Move to the next element
        
        return k  # Return the new length of the array with duplicates removed
prices = [100, 100, 100, 200, 200, 300]
solution = Solution()
new_length = solution.removeDuplicates(prices)

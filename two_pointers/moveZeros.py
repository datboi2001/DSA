class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Move all zeros to the end and maintain the order of non-zero elements.
        :param nums: 1d array of integers
        Do not return anything, modify nums in-place instead.
        """
        # Main idea: use two pointers, one to iterate through the array
        # and the other to keep track of the position of the next non-zero
        # element.
        # Time: O(n)
        
        # Edge case: empty array
        if len(nums) == 0:
            return
        
        # Initialize the pointer to the next non-zero element
        next_non_zero = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero, swap it with the next
            # non-zero element and increment the pointer to the next
            # non-zero element.
            if nums[i] != 0:
                nums[i], nums[next_non_zero] = nums[next_non_zero], nums[i]
                next_non_zero += 1

        

Solution().moveZeroes([0,1,0,3,12])
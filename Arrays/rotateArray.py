class Solution:
    
    def rotate(self, nums: list[int], k: int) -> None:
        """
        :param nums: List[int] the list of numbers
        :param k: int the number of rotations
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # Main idea: Reverse the entire list
        # Then, reverse the first k elements
        # Then, reverse the last n - k elements

        # Reverse the entire list
        i = 0
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1  
        # Reverse the first k elements
        i = 0
        j = k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        i = k
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """
        An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.


        :param nums: List[int]
        :return: Number of arithmetic subarrays
        """

        if len(nums) < 3:
            return 0
        # dp is the number of arithmetic subarrays ending at i
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

print(Solution().numberOfArithmeticSlices([1,2,3,4]))        
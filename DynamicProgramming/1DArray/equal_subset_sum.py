class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
        :param nums: List of numbers
        :return: True if we can partition the array into two subsets such that the sum of elements in both subsets is equal
        """
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        # dp[i] is True if we can make change for amount i
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]






print(Solution().canPartition([1, 2, 5]))
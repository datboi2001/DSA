class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Given an integer array nums, find a  subarray
        that has the largest product, and return the product.
        The test cases are generated so that the answer will fit in a 32-bit integer.
        :param nums: an array of integers
        :return: the maximum product of a contiguous subarray
        """

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Idea: Dynamic Programming. We can use dynamic programming to solve this problem. The main
        # idea is that if we want to find the maximum product of a contiguous subarray that ends at
        # index i, we can use the maximum product of a contiguous subarray that ends at index i - 1.
        # So the maximum product of a contiguous subarray that ends at index i is the maximum of the
        # following two cases:
        # 1. We use the number at index i
        # 2. We use the number at index i and the maximum product of a contiguous subarray that ends
        # at index i - 1

        # dp[i] is the maximum product of a contiguous subarray that ends at index i. dp[i][0] is
        # the maximum product and dp[i][1] is the minimum product (in case the array contains negative
        # numbers)
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            # We can use the number at index i
            dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            # Update the result
            result = max(result, dp[i][0])
        return result



print(Solution().maxProduct([-2, 3, -4]))
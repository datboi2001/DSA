class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        :param nums: list of integers
        :return: length of longest increasing subsequence
        """
        # Main idea: Dynamic Programming. The main idea is to maintain a table
        #  dp[i] which is the length of longest increasing subsequence ending
        #  with nums[i]. Then the state transition function is:
        # dp[i] = max(dp[j]) + 1, where 0 <= j < i and nums[j] < nums[i]
        # Base case: dp[i] = 1
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    # Update dp[i] if a longer increasing subsequence is found
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
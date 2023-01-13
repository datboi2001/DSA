class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        """
        Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
        :param arr: list of integers
        :param difference: difference between adjacent elements
        :return: length of longest subsequence such that difference between adjacent elements is equal to difference
        """
        # Main idea: dynamic programming. For each element, we need to know the length of the longest subsequence ending with this element.
        # We can use a dictionary to store the length of the longest subsequence ending with each element.
        # The length of the longest subsequence ending with arr[i] is 1 + the length of the longest subsequence ending with arr[i] - difference.
        # If arr[i] - difference is not in the dictionary, then the length of the longest subsequence ending with arr[i] is 1.

        # Time complexity: O(n)
        # Space complexity: O(n)
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1
        dp = {}
        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = 1 + dp[arr[i] - difference]
            else:
                dp[arr[i]] = 1
        return max(dp.values())
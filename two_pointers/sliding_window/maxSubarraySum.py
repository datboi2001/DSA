import sys
from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
    The length of the subarray is k, and
    All the elements of the subarray are distinct.
    Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
    A subarray is a contiguous non-empty sequence of elements within an array.
        :param nums: 1d array of integers
        :param k: size of the sliding window
        """ 
        # Main idea: use a sliding window and a hash table to keep track of
        # the elements in the window.

        window = Counter()
        max_sum = -sys.maxsize

        # Initialize the sliding window
        for i in range(k):
            window[nums[i]] += 1
        
        # Update the maximum subarray sum
        max_sum = max(max_sum, sum(window.keys()))

        # Slide the window
        for i in range(k, len(nums)):
            # Add the new element to the window
            window[nums[i]] += 1

            # Remove the oldest element from the window
            window[nums[i-k]] -= 1
            if window[nums[i-k]] == 0:
                del window[nums[i-k]]

            # Update the maximum subarray sum
            max_sum = max(max_sum, sum(window.keys()))
        
        return max_sum

print(Solution().maximumSubarraySum([1,5,4,2,9,9,9], 3))



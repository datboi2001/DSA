class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        # Idea: Use a set to store all the numbers. Then, for each number, check if the number before it is in the set.
        # If it is, then it is not the start of a sequence. Otherwise, it is the start of a sequence, so we can
        # iterate through the sequence and check how long it is. We can also remove the numbers from the set as we

        # iterate through them to avoid checking them again.
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        for num in nums:
            if num -1 not in nums_set:
                curr = num
                cur_length = 0
                while curr in nums_set:
                    curr += 1
                    cur_length += 1
                longest = max(longest, cur_length)
        return longest
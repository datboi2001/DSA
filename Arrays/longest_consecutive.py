class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_length = 0
        nums_set = set(nums)
        for num in nums:
            # check it's the start of a sequence
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest_length = max(longest_length, length)
        return longest_length

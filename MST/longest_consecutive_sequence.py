class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        :param nums: list of integers
        :return: length of longest consecutive sequence
        """
        if not nums:
            return 0
        max_len = 1
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num
                curr_len = 0
                while curr in nums_set:
                    curr += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len

print(Solution().longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
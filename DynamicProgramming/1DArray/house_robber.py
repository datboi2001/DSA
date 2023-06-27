from functools import cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_dp():
            rob1, rob2 = 0, 0
            # [rob1, rob2, n, n+1, ...]
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        @cache
        def rob_recursion(i: int):
            # Idea: Use recursion to solve the problem. The main idea is that
            # if we rob the ith house, we cannot rob the (i-1)th house. So the
            # maximum amount of money we can rob is the maximum of the following
            # two cases:
            # 1. Rob the ith house and the (i-2)th house
            # 2. Rob the (i-1)th house
            if i < 0:
                return 0
            result = max(rob_recursion(i-2) + nums[i], rob_recursion(i -1))
            return result
        
        return rob_recursion(len(nums)-1)
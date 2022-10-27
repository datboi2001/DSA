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
        
        def rob_recursion(memo: dict[int, int], i: int):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            result = max(rob_recursion(memo, i-2) + nums[i], rob_recursion(memo, i -1))
            memo[i] = result
            return result
        
        return rob_recursion({}, len(nums)-1)
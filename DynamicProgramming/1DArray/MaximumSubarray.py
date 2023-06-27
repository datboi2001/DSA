from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        local_sum = nums[0]
        for i in range(1, len(nums)):
            local_sum = max(nums[i], local_sum + nums[i])
            max_sum = max(max_sum, local_sum)
        return max_sum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
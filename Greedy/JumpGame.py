class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


print(Solution().canJump([2,0,0]))
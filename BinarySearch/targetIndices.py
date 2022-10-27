class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        lt, eq = 0, 0
        for num in nums:
            if num < target:
                lt += 1
            elif num == target:
                eq += 1
        return list(range(lt, lt + eq))
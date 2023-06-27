from functools import cache
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        You are given an integer array nums and an integer target.
        You want to build an expression out of nums by adding one of the symbols '+' and '-'
        before each integer in nums and then concatenate all the integers.
        For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to
        build the expression "+2-1".
        Return the number of different expressions that you can build, which evaluates to target. Note that
        you have to use all the elements in nums to build the expression.
        :param nums: an array of integers
        :param target: the target value
        """
         # Main idea: Recursion. We can use recursion to solve this problem. The main idea is that if we
         # want to make the expression that evaluates to target, we can either add or subtract the number
         # at index. So the number of different expressions that we can build is the sum of the following 
         # two cases:
            # 1. We add the number at index
            # 2. We subtract the number at index
        # Solve with recursion 
        @cache
        def find_recursion(index: int, target: int) -> int:
            if index == len(nums):
                return 1 if target == 0 else 0
            # You can either add or subtract the number at index
            return find_recursion(index + 1, target - nums[index]) + find_recursion(index + 1, target + nums[index])
        # Solve with dynamic programming
        return find_recursion(0, target)

if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    

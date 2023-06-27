from functools import cache, lru_cache
class Solution:
   # Time: O(n * k * target), Space: O(n * target)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        :param n: number of dice
        :param k: number of faces
        :param target: target value
        :return number of ways to get target value
        """
        @cache
        def dp(num_dice: int, total: int):
            if total > target or num_dice > n:
                return 0
            if total == target and num_dice == n:
                return 1
            ways = 0
            for val in range(1, k+1):
                total += val
                ways += dp(num_dice + 1, total)
                total -= val
            return ways
        return dp(0, 0) % (10 **9 + 7)
    
print(Solution().numRollsToTarget(30, 30, 500))

        
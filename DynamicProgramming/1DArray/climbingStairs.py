from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb_recursion(cur_steps: int, memo: dict[int, int]):
            # Add 1 if current_steps equals n
            if cur_steps == n:
                return 1
            # Add 0 if cur_steps is out of bound
            elif cur_steps > n:
                return 0
            # Recurrence relation is the number of ways if you start at step 1  + number of ways you start at step 2
            total_ways = climb_recursion(cur_steps + 1, memo) + climb_recursion(cur_steps + 2, memo)
            return total_ways
        
        def climb_bottom_up():
            dp = [0 for _ in range(n)]
            dp[n-1], dp[n-2] = 1, 1
            for i in range(n-3, -1, -1):
                dp[i] = dp[i + 1] + dp[i + 2]
            return dp[0]

        return climb_recursion(0, {})

    

    
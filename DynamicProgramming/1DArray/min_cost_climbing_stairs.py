from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        # iterate in reverse order
        for i in range(len(cost) -3, -1, -1):
            # The minimum cost to reach the top from ith staircase is the minimum cost of the next two staircases
            cost[i] += min(cost[i+1], cost[i + 2])
        # Return minimum of the first two staircases since we start can start from 0 or 1 index
        return min(cost[0], cost[1])
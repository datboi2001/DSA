from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [stone * -1 for stone in stones]
        heapify(stones)

        while stones:
            y = heappop(stones) * -1
            x = heappop(stones) * -1
            if x != y:
                heappush(stones, (y-x)*-1)
            if len(stones) == 1:
                break

        if len(stones) == 0:
            return 0
        return stones[0]*-1

print(Solution().lastStoneWeight([1]))
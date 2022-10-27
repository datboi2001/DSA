import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        hq.heapify(stones)
        while len(stones) > 1:
            first = hq.heappop(stones)
            second = hq.heappop(stones)
            if first == second:
                continue
            elif first < second:
                second -= first
                hq.heappush(stones, second * -1)
        if len(stones) == 1:
            return stones[0] * -1
        return 0

print(Solution().lastStoneWeight([2,7,4,1,8,1]))
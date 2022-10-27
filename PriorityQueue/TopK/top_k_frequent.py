from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return [nums[0]]
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        h = []
        for key, value in counter.items():
            heappush(h, (value, key))
            if len(h) > k:
                heappop(h)
        res = []
        while h:
            frq, item = heappop(h)
            res.append(item)
        return res
        
        
from collections import Counter
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return [nums[0]]
        counter = Counter(nums) 
        h = []
        for key, value in counter.items():
            heappush(h, (value, key))
            if len(h) > k:
                heappop(h)
        res = []
        while h:
            _, item = heappop(h)
            res.append(item)
        return res
        
        
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        bucket = [[] for _ in range(len(nums) + 1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num, times in count.items():
            bucket[times].append(num)
        for i in range(len(bucket) - 1, -1, -1):
            if len(ans) == k:
                return ans
            if len(bucket[i]) > 0:
                ans.extend(bucket[i])


print(Solution().topKFrequent([1], 1))

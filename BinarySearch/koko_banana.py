from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # The maximum range is the biggest number in the piles
        # The lower range is the average eating speed in h hours
        l, r = ceil(sum(piles) / h), max(piles)
        while l <= r:
            mid = (l + r) // 2
            # Find the number of hours it takes for Koko to eat all the bananas with
            # the current eating speed
            total_hours = 0
            for p in piles:
                total_hours += ceil(p/mid)
            # Cut off the left if total hours is bigger than the guard hours
            if total_hours > h:
                l = mid + 1
            # Cut off the right if total hours is smaller than the guard hours
            else:
                r = mid -1
        return l

print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
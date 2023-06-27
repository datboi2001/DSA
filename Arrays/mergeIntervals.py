class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Main idea: sort the intervals by the start time. Then iterate through the intervals and check if the current
        # interval overlaps with the previous interval. If it does, merge the intervals. If it doesn't, add the current
        if len(intervals) == 1:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

print(Solution().merge([[1,3], [2,5], [6,9]]))
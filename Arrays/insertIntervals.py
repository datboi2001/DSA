from bisect import bisect_left
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        :param intervals: intervals 
        :param newInterval: new interval to be inserted 
        :return: list of intervals after insertion. Merge overlapping intervals
        if necessary
        """
        new_index = bisect_left(intervals, newInterval)
        intervals.insert(new_index, newInterval)
        # Merging overlapping intervals
        result = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous intervals
                result[-1][1] = max(result[-1][1], interval[1])
        return result

print(Solution().insert([[1,3],[6,9]], [2,5]))
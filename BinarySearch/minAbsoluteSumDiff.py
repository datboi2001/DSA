from bisect import bisect_left
class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        if nums1 == nums2:
            return 0
        abs_diff_sum, abs_dif = 0, []
        min_diff_sum = float("inf")
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            abs_diff_sum += diff
            abs_dif.append(diff)
        nums1.sort()
        for num, diff in zip(nums2, abs_dif):
            index = bisect_left(nums1, num)
            if index > 0:
                min_diff_sum = min(min_diff_sum, abs_diff_sum - diff + abs(num - nums1[index-1]))
            if index < len(nums1):
                min_diff_sum = min(min_diff_sum, abs_diff_sum - diff + abs(num - nums1[index]))
        return min_diff_sum % (10**9 + 7)

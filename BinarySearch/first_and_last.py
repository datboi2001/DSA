

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums)-1
        ret = [-1, -1]
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if (nums[l] != target):
            return ret
        ret[0] = l
        r = len(nums) -1
        while l < r:
            mid = (l+r) // 2 + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        ret[1] = r
        return ret;
        


print(Solution().searchRange([5,7,7,8,8,10], 8))
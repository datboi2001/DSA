

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Main idea: use binary search to find the first position of target, and then use binary search to find the last
        # position of target.
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums)-1
        ret = [-1, -1]
        # Find the first position of target
        while l < r:
            mid = (l+r) // 2
            # If the mid is less than target, then the target must be in the right half
            if nums[mid] < target:
                l = mid + 1
            else:
                # If the mid is greater than target, then the target must be in the left half
                r = mid
        # If the target is not in the list, then return [-1, -1]
        if (nums[l] != target):
            return ret
        ret[0] = l
        r = len(nums) -1
        while l < r:
            # mid is rounded up, so the target must be in the right half
            mid = (l+r) // 2 + 1
            # If the mid is greater than target, then the target must be in the left half
            if nums[mid] > target:
                # If the mid is greater than target, then the target must be in the left half
                r = mid - 1
            else:
                # If the mid is less than target, then the target must be in the right half
                l = mid
        ret[1] = r
        return ret;
        


print(Solution().searchRange([5,7,7,8,8,10], 8))
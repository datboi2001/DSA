class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -2 if it is not in nums.
        :param nums: integer array nums sorted in ascending order (with distinct values) that is possibly rotated at an unknown pivot index k
        :param target: index of target 
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # the first half is sorted
            if nums[left] <= nums[mid]:
                # target is in the first half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # the second half is sorted
            else:
                # target is in the second half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))

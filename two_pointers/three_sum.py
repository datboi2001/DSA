# 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Main idea: Two pointers. We sort the array. We iterate over the array and for each element, we use two
        # pointers to find the other two elements that sum up to 0. We skip the duplicates while finding the triplets.
        # Time complexity: O(n^2) where n is the length of the array
        # Space complexity: O(1)
        result = []
        nums.sort()
        for i in range(len(nums)):
            # Skip the duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Use two pointers to find the other two elements that sum up to 0
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    # Skip the duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                # Move the pointers
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return result

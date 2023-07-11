class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        :param nums: list[int] a list of integers
        :return: list[list[int]] a list of quadruplets
        such that:
        1. The quadruplet contains unique elements
        nums[a], nums[b], nums[c], and nums[d] are distinct.
        2. nums[a] + nums[b] + nums[c] + nums[d] == target
        3. 0 <= a, b, c, d < len(nums)
        """
        # Main idea: Two pointers. We sort the array. We iterate over the array and for each element, we use two
        # pointers to find the other three elements that sum up to target. We skip the duplicates while finding the
        # quadruplets.

        # Time complexity: O(n^3) where n is the length of the array
        # Space complexity: O(1)
        result = []
        nums.sort()
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # Use three pointers to find the other three elements that sum up to target
            
            for b in range(a + 1, len(nums)):
                # Skip the duplicates
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        # Skip the duplicates
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
                    # Move the pointers
                    elif s < target:
                        c += 1
                    else:
                        d -= 1
        return result




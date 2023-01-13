import sys
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        :param nums: A list of integers
        :param target: A target integer
        :return: The sum of three integers in the list that is closest to the target.
        There is only one solution per input
        """
        # Idea: Sort the list. Use a sliding window to find the sum of three integers that is closest to the target.
        # The main idea is that we sort the list first. Then we use a sliding window to find the sum of three integers
        # that is closest to the target.

        nums.sort()
        closest_sum = sys.maxsize 
        # Loop through the list. For each element, we use a sliding window to find the sum of three integers that is
        # closest to the target.
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) -1
            # Use a sliding window to find the sum of three integers that is closest to the target.
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                # If the sum of three integers is equal to the target, we return the sum.
                if current_sum == target:
                    return current_sum
                # If the sum of three integers is closer to the target than the previous sum, we update the closest_sum.
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                # If the sum of three integers is less than the target, we move the left pointer to the right.
                if current_sum < target:
                    left += 1
                # If the sum of three integers is greater than the target, we move the right pointer to the left.
                else:
                    right -= 1
        return closest_sum

# Time complexity: O(n^2). n is the length of the list. Sorting the list takes O(nlogn). We traverse the list once using
# a sliding window. The sliding window takes O(n) time. Therefore, the time complexity is O(nlogn) + O(n) = O(n^2).
# Space complexity: O(1). We use a constant amount of space to store the closest_sum.

print(Solution().threeSumClosest([-1,2,1,-4], 1))


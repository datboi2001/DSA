class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        :param nums: list of integers
        :param val: integer
        :return: length of the new list after removing all the elements of value val
        """
        # Main idea: use two pointers. One pointer is used to iterate through the list, and the other pointer is used to
        # keep track of the position to insert the next element that is not equal to val.

        if not nums:
            return 0
        first = 0
        second = 0

        # Iterate through the list
        while first < len(nums):
            if nums[first] != val:
                # If the element is not equal to val, then insert it at the position of second pointer
                nums[second] = nums[first]
                second += 1
            first += 1
        return second


print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
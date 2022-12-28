class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        :param nums: list of integers. Each element in the array represents your maximum jump length at that position.
        :return: boolean indicating if you can reach the last index
        """
        if not nums:
            return False
        if len(nums) == 1:
            return True
        # max_reach is the maximum index that can be reached from the current index
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            # update max_reach
            max_reach = max(max_reach, i + nums[i])
        return True


print(Solution().canJump([3,2,1,0,4]))
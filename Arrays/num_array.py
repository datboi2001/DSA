class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.running_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.running_sum.append(self.running_sum[-1] + nums[i])
            

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.running_sum[right]
        return self.running_sum[right] - self.running_sum[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
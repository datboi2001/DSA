class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        index = -1
        for i in range(len(prefix_sum)):
            if i == 0: 
                if  0 == prefix_sum[-1] - prefix_sum[0]:
                    index = i
                    break
            elif i == len(prefix_sum) -1:
                if prefix_sum[i-1] == 0:
                    index = i
                    break
            else:
                if prefix_sum[i-1] == prefix_sum[-1] - prefix_sum[i]:
                    index = i
                    break
        return index

print(Solution().pivotIndex([0,-1,-1,-1,-1,-1]))
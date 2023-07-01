from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        cur_count = 0
        prev_element = None
        ans = []
        majority_count = floor(len(nums) / 3)
        for num in nums:
            
            
            prev_element = num
        return ans
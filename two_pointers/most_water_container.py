class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            cur_area = (right-left) * min(height[left], height[right])
            max_area = max(max_area, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
        

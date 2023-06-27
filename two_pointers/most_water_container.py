class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # The area is the width times the height
            cur_area = (right-left) * min(height[left], height[right])
            # Update the max area
            max_area = max(max_area, cur_area)
            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                # If the heights are the same or bigger, then move the left pointer
                right -= 1
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
        

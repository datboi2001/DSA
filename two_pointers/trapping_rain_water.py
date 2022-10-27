from typing import List

def trapping_rain_water(height: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if not height:
        return 0
    total = 0
    left, right = 0, len(height) - 1
    leftMax, rightMax = height[left], height[right]
    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            total += (leftMax - height[left])
        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            total += (rightMax - height[right])
    return total

if __name__ == '__main__':
    elevations = [int(x) for x in input().split()]
    res = trapping_rain_water(elevations)
    print(res)

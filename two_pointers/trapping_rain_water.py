
def trapping_rain_water(height: list[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it can trap after raining.
    :param height: list of heights
    :return: amount of water trapped
    """
    if not height:
        return 0 
    l, r = 0, len(height) - 1
    l_max, r_max = height[l], height[r]
    water = 0
    while l < r:
        # if left is lower than right, then we know that the left side is bounded by left_max
        l_max = max(l_max, height[l])
        # If right is lower than left, then we know that the right side is bounded by right_max
        r_max = max(r_max, height[r])
        # if left side is lower, we can trap water on the left side
        if l_max < r_max:
            water += l_max - height[l]
            l += 1
        # If right side is lower, we can trap water on the right side
        else:
            water += r_max - height[r]
            r -= 1
    return water
if __name__ == '__main__':
    elevations = [int(x) for x in input().split()]
    res = trapping_rain_water(elevations)
    print(res)

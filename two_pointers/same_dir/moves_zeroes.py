from typing import List

def move_zeros(nums: List[int]) -> None:
    # WRITE YOUR BRILLIANT CODE HERE
    slow = fast = 0
    while slow < len(nums) and fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))

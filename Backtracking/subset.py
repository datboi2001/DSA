from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(list(subset))
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision to exclude nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res



if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = subsets(nums)
    res = [' '.join(str(x) for x in sorted(subset)) for subset in res]
    res.sort()
    for row in res:
        print(row)

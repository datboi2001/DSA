class Solution:
    def solve(self, arr):
        l, r = 0, len(arr)-1
        ans = arr[0]
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] > ans:
                ans = arr[mid]
                l = mid + 1
            else:
                r = mid - 1
        return ans

print(Solution().solve([0, 1]))

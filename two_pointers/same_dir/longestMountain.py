class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        max_len = 0
        state, length = 0, 1
        for i in range(len(arr) - 1):
            if state in [0,1] and arr[i] < arr[i+1]:
                state = 1
                length += 1
            elif state == 2 and arr[i] < arr[i+1]:
                state = 1
                length = 2
            elif state in [1, 2] and arr[i] > arr[i+1]:
                state = 2
                length += 1
                max_len = max(length, max_len)
            else:
                state = 0
                length = 1
        return max_len
print(Solution().longestMountain([875, 884, 239, 731, 723, 685]))

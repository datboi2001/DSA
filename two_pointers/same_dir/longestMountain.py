class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        max_len = 0
        # 0: flat, 1: up, 2: down
        state, length = 0, 1
        for i in range(len(arr) - 1):
            if state in [0,1] and arr[i] < arr[i+1]:
                # If the state is flat or up, and the next number is bigger, then
                # we are still going up
                state = 1
                length += 1
            elif state == 2 and arr[i] < arr[i+1]:
                # If the state is down, and the next number is bigger, then we
                # are going up again
                state = 1
                length = 2
            elif state in [1, 2] and arr[i] > arr[i+1]:
                # If the state is up or down, and the next number is smaller,
                # then we are going down
                state = 2
                length += 1
                max_len = max(length, max_len)
            else:
                # If the state is flat or up, and the next number is smaller,
                # then we are going down
                state = 0
                length = 1
        return max_len
print(Solution().longestMountain([875, 884, 239, 731, 723, 685]))

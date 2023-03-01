class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """
        Given the array arr, replace every lements in the array with the greatest
        element among the elements to its right, and replace the last element with -1.
        :param arr: an array of integers
        :return: an array of integers
        """
        # Main idea: traverse the array from right to left, and keep track of the
        # maximum value seen so far.
        # Time complexity: O(n)
        max_val = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) -1:
                arr[i] = -1
            else:
                prev_ele = arr[i]
                arr[i] = max_val
                if prev_ele > max_val:
                    max_val = prev_ele
        return arr


print(Solution().replaceElements([17,18,5,4,6,1]))
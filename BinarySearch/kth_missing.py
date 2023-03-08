class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        """
        :param arr: list of positive integers in sorted order
        :param k: positive integer
        :return: kth missing positive integer that is missing from this array
        """
        # Main idea: find the first missing number.
        #  If the difference between the current number and the index is greater than k, then the kth missing number is k + i.
        # If the difference between the last number and the index is less than k, then the kth missing number is k + len(arr). 
        if k < arr[0]:
            return k
        
        # find the first missing number
        for i in range(len(arr)):
            # if the difference between the current number and the index is greater than k
            if arr[i] - i - 1 >= k:
                return k + i
        # if the difference between the last number and the index is less than k
        return k + len(arr)

print(Solution().findKthPositive([1,2,3,4], 2))

import heapq as hq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        :param nums: list[int]
        :param k: int
        :return: kth largest element in the array 
        """
        return hq.nlargest(k, nums)[-1]

# Time complexity: O(nlogn)

if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))

class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        """
        :param candies: candies[i] is the number of candies in the ith box. You can divide the candies in any box
        but cannot add or remove any candies from any box.
        :param k: The numbber of children you should allocate the candies to.
        :return: The maximum number of candies you can allocate to the children.
        """
        # Main idea: Binary search. The maximum number of candies you can allocate to the children is the maximum
        # number of candies in any box. So we can binary search for the maximum number of candies in any box.
        # Then we can check if we can allocate the candies to the children with this maximum number of candies.
        # If we can, we can increase the maximum number of candies in any box. If we cannot, we can decrease the
        # maximum number of candies in any box.
        left, right = 0, sum(candies) / k
        while left < right:
            mid = (left + right + 1) // 2
            if k > sum(a / mid for a in candies):
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == '__main__':
    print(Solution().maximumCandies([5, 8 ,6], 3))
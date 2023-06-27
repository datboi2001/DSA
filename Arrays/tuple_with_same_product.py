from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        """
        Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
        :param nums: a list of integers
        :return: The number of tuples (a, b, c, d) such that a * b = c * d
        """
        # Main idea: use a dictionary to store the product of two numbers and the number of times it appears
        # Then we iterate through the dictionary and calculate the number of tuples
        # The number of tuples is the number of times a product appears times the number of times it appears minus 1
        # We divide by 2 because we are counting the same tuple twice

        # Create a dictionary to store the product of two numbers and the number of times it appears
        product_dict = defaultdict(int)
        ans = 0
        # Loop through all possible combinations of two numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Store the product of the two numbers
                product = nums[i] * nums[j]
                # Increment the number of times the product appears
                # If the product is 6, then product_dict[6] = 1
                ans += product_dict.get(product, 0)
                product_dict[product] += 1
        # Answer is 8 * ans because we are counting the same tuple 8 times
        return 8 * ans
print(Solution().tupleSameProduct([2,3,4,6]))
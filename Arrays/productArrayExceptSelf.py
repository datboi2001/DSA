class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        :param nums: an array nums of n integers where n > 1
        :return: an array output such that output[i] is equal to the product of all the elements of nums except nums[i]
        """

        # Main idea: we need to calculate the product of all elements to the left of the current element
        # and the product of all elements to the right of the current element
        # and then multiply them

        left_multiplication: list[int] = [1] * len(nums)
        right_multiplication: list[int] = [1] * len(nums)
        result: list[int] = [1] * len(nums)
        for i in range(1, len(nums)):
            left_multiplication[i] = left_multiplication[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_multiplication[i] = right_multiplication[i+1] * nums[i+1] 
        for i in range(len(nums)):
            result[i] = left_multiplication[i] * right_multiplication[i]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))
    print(solution.productExceptSelf([-1,1,0,-3,3]))
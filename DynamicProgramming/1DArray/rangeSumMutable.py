class NumArray:

    def __init__(self, nums: list[int]):
        """
        Given an integer array nums, handle multiple queries of the following types:
        Update the value of an element in nums.
        Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
        :param nums: List[int]
        """        
        
        # Idea: Use a segment tree to store the sum of each node
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Initialize the segment tree
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        # Build the segment tree
        for i in range(self.n, 2 * self.n):
            # The leaf nodes are the values of the array
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            # The parent node is the sum of the left and right child
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]




    def update(self, index: int, val: int) -> None:
        """
        :param index: int
        :param val: int
        :return: None
        """ 
        # Idea: Update the value of the node in the segment tree
        # Time complexity: O(logn)

        # Update the value of the node in the segment tree
        index += self.n

        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            # If the index is even, the left child is the index + 1
            if index % 2 == 0:
                right = index + 1
            else:
                # If the index is odd, the right child is the index - 1
                left = index - 1

            # Update the value of the parent node
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2
        


    def sumRange(self, left: int, right: int) -> int:
        """
        :param left: int
        :param right: int
        left <= right
        :return: int
        """

        # Idea: Use the segment tree to calculate the sum of the range
        # Time complexity: O(logn)

        # Initialize the sum
        result = 0

        # Calculate the sum of the range
        left += self.n
        right += self.n
        while left <= right:
            # If the left index is odd, add the value of the left index to the sum
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            # If the right index is even, add the value of the right index to the sum
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
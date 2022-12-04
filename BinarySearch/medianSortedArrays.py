class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        The overall time complexity should be O(log(m+n)). Use binary search
        to solve the problem
        :param nums1: sorted array
        :param nums2: sorted array
        :return: median of two sorted arrays
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            # mid is the index of the first element in the right half of nums1
            mid2 = (m + n + 1) // 2 - mid
            # mid2 is the index of the first element in the right half of nums2
            if mid > 0 and nums1[mid - 1] > nums2[mid2]:
                # mid is too big, need to move it to the left
                right = mid - 1
            elif mid < m and nums1[mid] < nums2[mid2 - 1]:
                # mid is too small, need to move it to the right
                left = mid + 1
            else:
                if mid == 0:
                    # all elements in nums1 are in the right half
                    max_left = nums2[mid2-1]
                elif mid2 == 0:
                    # all elements in nums2 are in the right half
                    max_left = nums1[mid-1]
                else:
                    # find the max of the left half
                    max_left = max(nums1[mid-1], nums2[mid2-1])
                if (m + n) % 2 == 1:
                    # odd number of elements, return the max of the left half
                    return max_left
                if mid == m:
                    # all elements in nums1 are in the left half
                    min_right = nums2[mid2]
                elif mid2 == n:
                    # all elements in nums2 are in the left half
                    min_right = nums1[mid]
                else:
                    # find the min of the right half
                    min_right = min(nums1[mid], nums2[mid2])
                # even number of elements, return the average of the two middle elements
                return (max_left + min_right) / 2


print(Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

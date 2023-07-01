class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        :param nums1: An integer array
        :param nums2: An integer array
        :return: An intersection of the two arrays
        """
        if nums1 == nums2:
            return nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Main idea: Binary search for each element in nums1 in nums2.
        # Time: O(nlogm) where n is the length of nums1 and m is the length of nums2
        # Space: O(n) where n is the length of nums1

        # Sort nums1 and nums2.
        nums1.sort()
        nums2.sort()

        # Create a list to store the intersection of nums1 and nums2.
        intersection = []

        # For each element in nums1, binary search for the element in nums2.
        for num in nums1:
            l, r = 0, len(nums2) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums2[mid] == num:
                    intersection.append(num)
                    nums2.pop(mid)
                    break
                elif nums2[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
        return intersection



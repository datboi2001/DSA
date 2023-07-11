
def merge(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    You can assume that nums1 have enough space (size that is greater or equal to m + n)
    """
    # Main idea: merge from the end of the array
    # Time: O(m + n)
    # Space: O(1)
    m, n = len(nums1), len(nums2)
    i, j = m - 1, n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
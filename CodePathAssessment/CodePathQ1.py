def merge(nums1, nums2):
    if not nums1 and not nums2:
        return []
    result = []
    i = j =0
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                i += 1
        elif i < len(nums1):
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    return result
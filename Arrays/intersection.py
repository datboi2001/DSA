def intersection(a: list[int], b: list[int]) -> list[int]:
    """
    :param a: An integer array
    :param b: An integer array
    :return: An intersection of the two arrays
    """
    # Time complexity: O(n + m) where n is the length of a and m is the length of b
    # Space complexity: O(n + m) where n is the length of a and m is the length of b
    return list(set(a) & set(b))
from typing import List, Tuple
def connected_segments(segments: List[Tuple[int, int, int]]):
    """
    You are given n colored segments on the number line.
    Each segment is either colored red or blue.
    The i-th segment can be represented by a tuple (ci,li,ri).
    The segment contains all the points in the range [li,ri], inclusive, and its color denoted by ci:

    if ci=0, it is a red segment;
    if ci=1, it is a blue segment.
    We say that two segments of different colors are connected, if they share at least one common point.
    Two segments belong to the same group, if they are either connected directly,
    or through a sequence of directly connected segments. Find the number of groups of segments.
    :param segments: list of segments
    :return: number of connected segments
    """
    if not segments:
        return 0
    segments.sort(key=lambda x: x[1])
    roots = [-1] * len(segments)

    def find(n):
        if roots[n] < 0:
            return n
        else:
            res = find(roots[n])
            roots[n] = res
            return res

    def union(i, j):
        ri = find(i)
        rj = find(j)
        size1 = roots[ri] * -1
        size2 = roots[rj] * -1
        if size1 < size2:
            roots[ri] = rj
            roots[rj] = (size1 + size2) * -1
        else:
            roots[rj] = ri
            roots[ri] = (size1 + size2) * -1

    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            if segments[i][0] != segments[j][0] and segments[i][2] >= segments[j][1]:
                union(i, j)
    return len([root for root in roots if root < 0])

# Time complexity: O(n^2)
# Space complexity: O(n)

num_test_cases = int(input())
for _ in range(num_test_cases):
    num_segments = int(input())
    segments = []
    for _ in range(num_segments):
        segments.append(tuple(int(i) for i in input().split()))
    print(connected_segments(segments))

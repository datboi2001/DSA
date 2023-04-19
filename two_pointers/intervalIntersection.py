class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        """
        You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

        Return the intersection of these two interval lists.

        A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

        The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
        
        :param firstList: list of closed intervals
        :param secondList: list of closed intervals
        :return: intersection of these two interval lists
        """

        # Main idea: two pointers. We start from the first interval in the first list
        # and the first interval in the second list.
        # If the first interval in the first list starts before the first interval in the second list,
        # we move to the next interval in the first list. If the first interval in the first list starts
        # after the first interval in the second list, we move to the next interval in the second list.
        # Time complexity: O(n + m)

        # Initialize the result list
        res = []

        # Initialize the two pointers
        i = 0
        j = 0

        # While the two pointers are within the bounds of the lists
        while i < len(firstList) and j < len(secondList):
            # If the first interval in the first list starts before the first interval in the second list
            if firstList[i][0] < secondList[j][0]:

                # If the first interval in the first list ends before the first interval in the second list
                # starts, we move to the next interval in the first list
                if firstList[i][1] < secondList[j][0]:
                    i += 1

                # If the first interval in the first list ends after the first interval in the second list
                # starts, we add the intersection to the result list and move to the next interval in the
                # first list
                elif firstList[i][1] >= secondList[j][0]:
                    res.append([secondList[j][0], min(firstList[i][1], secondList[j][1])])
                    i += 1
            
            # If the first interval in the first list starts after the first interval in the second list
            else:
                    # If the first interval in the second list ends before the first interval in the first list
                    # starts, we move to the next interval in the second list
                    if secondList[j][1] < firstList[i][0]:
                        j += 1
                    # If the first interval in the second list ends after the first interval in the first list
                    # starts, we add the intersection to the result list and move to the next interval in the
                    # second list
                    elif secondList[j][1] >= firstList[i][0]:
                        res.append([firstList[i][0], min(firstList[i][1], secondList[j][1])])
                        j += 1

        return res


if __name__ == '__main__':
    print(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
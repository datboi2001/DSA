from collections import defaultdict
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        :param n: int
        :param k: int
        :return: a list of lists of integers representing all possible combinations of k numbers out of 1 ... n
        """
        # Main idea: DFS. The main idea is to use DFS to find all possible combinations. The key is to use a set to store the visited elements to avoid duplicates.
        # We can avoid duplicates by using a set to store the visited elements. For example, if we have a list [1, 2, 3], we can use a set to store the visited elements, and then we can avoid the duplicates like [1, 2, 3] and [1, 3, 2].
        # Time complexity: O(n^k)
        result = []
        seen = set() 
        def dfs(start, path):
            if len(path) == k:
                result.append(list(path))
                return
            for i in range(start, n + 1):
                if i in seen:
                    continue
                path.append(i)
                seen.add(i)
                dfs(i + 1, path)
                path.pop()
                seen.remove(i)
        dfs(1, [])
        return result

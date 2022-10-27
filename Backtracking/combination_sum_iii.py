class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        :param k: length of the combination list
        :param n: Target sum
        :return: All valid combinations of k numbers that sum up 
        to n
        """
        def dfs(k: int, n: int, i: int, cur: list[int], res: list[list[int]]):
            """
            :param k: length of the combination list
            :param n: Target sum
            :param i: current number
            :param cur: current combination list
            :param res: result list
            """
            if k == 0 and n == 0:
                res.append(list(cur))
                return
            if k == 0 or n == 0:
                return
            for j in range(i, 10):
                
                cur.append(j)
                dfs(k - 1, n - j, j + 1, cur, res)
                cur.pop()
        res = []
        dfs(k, n, 1, [], res)
        return res

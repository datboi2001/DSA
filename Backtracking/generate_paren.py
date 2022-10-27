class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        :param n: Give n pairs of parentheses 
        :return: Return all combinations of well-formed parentheses
        """

        def backtrack(res: list[str], s: str, left: int, right: int):
            """
            :param res: The result list
            :param s: The current string
            :param left: The number of left parentheses
            :param right: The number of right parentheses
            """
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(res, s + '(', left + 1, right)
            if right < left:
                backtrack(res, s + ')', left, right + 1)
        res = []
        backtrack(res, '', 0, 0)
        return res

print(Solution().generateParenthesis(3))
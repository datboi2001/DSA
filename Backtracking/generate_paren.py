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
            # If the length of the string is equal to 2 * n, we have a valid string
            if len(s) == 2 * n:
                res.append(s)
                return
            # If the number of left parentheses is less than n, we can add a left parenthesis
            # because we can't have more left parentheses than n
            if left < n:
                backtrack(res, s + '(', left + 1, right)
            # If the number of right parentheses is less than the number of left parentheses, we can add a right parenthesis
            # because we can't have more right parentheses than left parentheses
            if right < left:
                backtrack(res, s + ')', left, right + 1)
        res = []
        backtrack(res, '', 0, 0)
        return res

print(Solution().generateParenthesis(3))
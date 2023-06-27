class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        """
        :param matchsticks: A list of integers indicating the length of the matches
        :return: A boolean indicating if it's possible to make a square out of the sticks
        """
        if not matchsticks:
            return False
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side = perimeter // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        sides = [0] * 4
        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for i in range(4):
                if sides[i] + matchsticks[index] > side:
                    continue
                j = i -1
                while j >= 0:
                    if sides[i] == sides[j]:
                        break
                    j -= 1
                if j != -1:
                    continue
                sides[i] += matchsticks[index]
                if backtrack(index + 1):
                    return True
                sides[i] -= matchsticks[index]
            return False
        return backtrack(0)

print(Solution().makesquare([3, 3, 3, 3, 4]))
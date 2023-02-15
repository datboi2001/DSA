from functools import cache

def maximum_score(candies: list[int], candy_type: int) -> int:
    """
    :param candies: list of candies held by each animal
    :param candy_type: the type of candy you are holding
    :return: the maximum possible score you can earn by visiting the animals in order from 1 to n
    """
    @cache
    def max_score_recursion(i: int, c: int) -> int:
        if i == len(candies):
            return 0
        if candies[i] == c:
            return max_score_recursion(i + 1, c) + 1
        else:
            return max(max_score_recursion(i + 1, candies[i])-1, max_score_recursion(i + 1, c))

    def max_score_dp() -> int:
        # Idea: dp[i][j] = max score if we are at index i and we have candy type j
        # Base case: dp[n][j] = 0
        # Transition: dp[i][j] = max(dp[i+1][j], dp[i+1][candies[i]]-1) if candies[i] != j
        #             dp[i][j] = dp[i+1][j] + 1 if candies[i] == j
        # dp[i][j] = max score if we are at index i and we have candy type j
        dp = [[0 for _ in range(5)] for _ in range(len(candies) + 1)]
        # Loop backward because we need to know the max score at index i+1
        for i in range(len(candies) - 1, -1, -1):
            for j in range(0, 5):
                if candies[i] != j:
                    # We can either keep the same candy type or exchange it for the candy type of the current animal
                    dp[i][j] = max(dp[i + 1][j], dp[i + 1][candies[i]] - 1)
                else:
                    # We exchange the candy type for the candy type of the current animal
                    dp[i][j] = dp[i + 1][j] + 1
        return dp[0][candy_type]

    return max_score_dp()

    # Test case 1
candy_types = [1, 2, 2, 2, 3]
candy_type = 0
print(maximum_score(candy_types, candy_type))  # 1

# Test case 2
candy_types = [1, 2, 2, 2, 3]
candy_type = 2
print(maximum_score(candy_types, candy_type))  # 3

# Test case 3
candy_types = [1, 2, 2, 2, 3]
candy_type = 3
print(maximum_score(candy_types, candy_type))  # 1

# Test case 4
candy_types = [1, 2, 2, 2, 3]
candy_type = 4
print(maximum_score(candy_types, candy_type))  # 1

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
        Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
        On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
        The game continues until all the stones have been taken.
        Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
        :param piles: 1d array of integers
        :return: maximum number of stones Alice can get
        """
        # Main idea: Dynamic Programming. Use a 2D array to keep track of the
        # maximum number of stones Alice can get if she starts at pile i with
        # M = j. 
        # Time: O(n^2)
        # Space: O(n^2)
        
        # Initialize the 2D array
        n = len(piles)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # Calculate the suffix sum of the piles
        suffix_sum = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]
        
        # Calculate the maximum number of stones Alice can get if she starts
        # at pile i with M = j
        for i in range(n-1, -1, -1):
            for j in range(n, 0, -1):
                # If there are not enough piles left, then Alice can take all
                # the remaining piles
                if i + 2 * j >= n:
                    dp[i][j] = suffix_sum[i]
                # Otherwise, Alice can take all the remaining piles or take
                # some piles and let Bob take the rest
                else:
                    for x in range(1, 2*j+1):
                        dp[i][j] = max(dp[i][j], suffix_sum[i] - dp[i+x][max(x, j)])
        return dp[0][1]
        
print(Solution().stoneGameII([1,2,3,4,5,100]))

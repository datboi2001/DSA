class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        :param secret: String
        :param guess: String
        :return: A string in the format of "xAyB", where A is the number of bulls and B is the number of cows
        """
        if len(secret) != len(guess):
            return "0A0B"
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        for i in range(10):
            # count the number of each digit in secret and guess
            # the minimum of the two is the number of cows
            cows += min(secret.count(str(i)), guess.count(str(i)))
        return f"{bulls}A{cows - bulls}B"

# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().getHint("1123", "0111"))
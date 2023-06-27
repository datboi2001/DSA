class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        """
        Alice is texting Bob using her phone. 
        The mapping of digits to letters is similar to the one on a standard phone. 
        In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.
        However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.
        Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.
        Since the answer may be very large, return it modulo 10^9 + 7.
        :param pressedKeys: string
        :return the total number of text messages that can be sent using the given sequence of key presses
        """
        # dp[i] represents the number of text messages that can be sent using the first i key presses
        dp: list[int | float] = [0] * (len(pressedKeys) + 1)

        # Base case. 
        dp[0] = 1
        mod = pow(10, 9) + 7
        # Iterate through the given sequence of key presses
        for i in range(1, len(pressedKeys) + 1):
            
            dp[i] = dp[i-1] % mod
            if i -2 >= 0 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] = (dp[i] + dp[i-2]) % mod
                if i - 3 >= 0 and pressedKeys[i-1] == pressedKeys[i-3]:
                    dp[i] = (dp[i] + dp[i-3]) % mod 
                    if pressedKeys[i-1] in '79' and i - 4 >= 0 and pressedKeys[i-4] == pressedKeys[i-1]:
                        dp[i] = (dp[i] + dp[i-4]) % mod
        return dp[-1]  


print(Solution().countTexts('22233'))


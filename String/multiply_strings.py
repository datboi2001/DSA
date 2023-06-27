class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        :param num1: str
        :param num2: str
        :return: product of num1 and num2, represented as a string. Cannot convert to int directly
        """
        # Idea is to multiply each digit of num1 with num2 and add the result to the final result
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        # Reverse the string to make it easier to multiply
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                # i + j is the index of the result
                result[i + j] += int(num1[i]) * int(num2[j])
        # Loop through the result and add the carry to the next digit
        for i in range(len(result) - 1):
            # Add the carry to the next digit
            result[i + 1] += result[i] // 10
            # Update the current digit
            result[i] %= 10
        while result[-1] == 0:
            result.pop()
        return "".join([str(i) for i in reversed(result)])

print(Solution().multiply("123", "456"))

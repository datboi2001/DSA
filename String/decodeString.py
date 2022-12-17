class Solution:
    def decodeString(self, s: str) -> str:
        """
        :param s: encoded string. The encoding rule is k[encoded_string],
        where the encoded_string inside the square brackets is being repeated exactly k times.
        :return: decoded string
        """
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # pop the string to be repeated
                sub = []
                while stack[-1] != "[":
                    sub.append(stack.pop())
                stack.pop()
                # pop the number of times to repeat
                num = "" 
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num 
                # push the repeated string
                num = int(num)
                stack.append("".join(sub[::-1])*num)
        return "".join(stack)

print(Solution().decodeString("3[a]2[bc]"))

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        if not k:
            return num
        stack = []
        for i in range(0, len(num)):
            while len(stack) > 0 and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            if stack or num[i] != '0':
                stack.append(num[i])
        if k:
            stack = stack[0:-k]
        return ''.join(stack) or '0'

print(Solution().removeKdigits("1432219", 3))

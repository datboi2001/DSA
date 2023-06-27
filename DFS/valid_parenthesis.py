class Solution:
    def isValid(self, s: str) -> bool:
        brackets_maps = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for bracket in s:
            if bracket in brackets_maps:
                stack.append(bracket)
            else:
                if len(stack) > 0 and bracket == brackets_maps[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for a in s:
            if a == "#" and len(stack1) > 0:
                stack1.pop()
            elif a != "#":
                stack1.append(a)
        for b in t: 
            if b == "#" and len(stack2) > 0:
                stack2.pop()
            elif b != "#":
                stack2.append(b)
        # print(stack1)
        # print(stack2)
        return stack1 == stack2
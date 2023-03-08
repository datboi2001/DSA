class Solution:
    def isValid(self, s: str) -> bool:
        """
        A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.
        :param s: a target string
        """
        # Main idea: use a stack to store the characters in s.
        # If the current character is 'c', then pop the last two characters from the stack and check if they are 'a' and 'b' respectively.
        # If not, then return False.

        if not s:
            return True
    
        stack = []
        for c in s:
            if c == 'c':
                if len(stack) < 2:
                    return False
                if stack.pop() != 'b' or stack.pop() != 'a':
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

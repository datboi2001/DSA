class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        Return true if and only if we can swap two letters in s so that the result equals goal.
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # main idea: if s and goal are equal, then we need to check if there are at least two
        # same letters in s. If s and goal are not equal, then we need to check if there are
        # exactly two different letters in s and goal, and if we can swap them to make s equal
        # to goal.
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        else:
            diff = [(x, y) for x, y in zip(s, goal) if x != y]
            return len(diff) == 2 and diff[0] == diff[1][::-1]
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
        Return the minimum number of boats to carry every given person.
        :param people: list where  each element is the weight of the ith person
        :param limit: weight limit for each boat
        :return: the minimum number of boats needed to carry all people
        """
        # Main idea: sort the list and use two pointers to find the minimum number of boats

        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            # if the heaviest person can be carried with the lightest person, then we can use one boat
            if people[left] + people[right] <= limit:
                left += 1
            # if the heaviest person cannot be carried with the lightest person, then we need to use one boat for the heaviest person
            right -= 1
            boats += 1
        return boats
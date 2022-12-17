from queue import PriorityQueue


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
        :param stones: list of stones weight
        :return: the weight of the last stone. If there are no stones left, return 0.
        """
        pq = PriorityQueue()
        for stone in stones:
            pq.put(-stone)
        while pq.qsize() > 1:
            y = pq.get()
            x = pq.get()
            if x != y:
                pq.put(y - x)
        if pq.qsize() == 1:
            return -pq.get()
        else:
            return 0

print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
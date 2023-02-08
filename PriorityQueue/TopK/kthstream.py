from heapq import heappush, heappop
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.nums = []
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]


obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

from heapq import heappop, heappush

class MedianOfStream:

    # Idea: use two heaps, one max heap and one min heap.
    # The max heap stores the smaller half of the numbers, and the min heap stores the larger half of the numbers.
    # The max heap and the min heap are balanced, so that the median can be found in O(1) time.
    # Time complexity: O(logn) for add_number, O(1) for get_median
    # Space complexity: O(n)

    def __init__(self):
        # Max Heap
        self.small = []

        # Min Heap
        self.large = []

    def add_number(self, num: float) -> None:
        # WRITE YOUR BRILLIANT CODE HERE
        heappush(self.small, -num)

        # make sure every num in small <= ever num in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heappop(self.small)
            heappush(self.large, val)

        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = -heappop(self.large)
            heappush(self.small, val)


    def get_median(self) -> float:
        # ALSO HERE
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    median_of_stream = MedianOfStream()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        if line == 'get':
            median = median_of_stream.get_median()
            print(f'{median:.1f}')
        else:
            num = float(line)
            median_of_stream.add_number(num)

from heapq import heappush, heappop
def nth_ugly_number(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    min_heap = [1]
    used_nums = {1}
    allowed_primes = (2, 3, 5)
    cur_val = None
    for _ in range(n):
        cur_val = heappop(min_heap)
        for prime in allowed_primes:
            next_val = prime * cur_val
            if next_val not in used_nums:
                heappush(min_heap, next_val)
                used_nums.add(next_val)
    return cur_val


if __name__ == '__main__':
    n = int(input())
    res = nth_ugly_number(n)
    print(res)

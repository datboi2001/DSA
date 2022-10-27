from collections import Counter
from heapq import heapify, heappop, heappush

def reorganize_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    counts = Counter(s)
    res = ""
    maxHeap = [[-cnt, char] for char, cnt in counts.items()]
    heapify(maxHeap)

    prev = None

    while len(maxHeap) > 0 or prev is not None:
        if prev and len(maxHeap) == 0:
            return ""
        # most frequent char, except prev
        cnt, char = heappop(maxHeap)
        res += char
        cnt += 1

        if prev:
            heappush(maxHeap, prev)
            prev = None

        if cnt < 0:
            prev = [cnt, char]
    return res


if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i+1}")
            exit()
    print("Valid")

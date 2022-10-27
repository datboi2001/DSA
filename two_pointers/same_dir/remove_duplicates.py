from typing import List

def remove_duplicates(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    i = j = 0
    while i < len(arr) and j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            j += 1
        else:
            j += 1
    return i + 1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))

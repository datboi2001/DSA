from collections import Counter
from typing import List


def is_anagram(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)


def find_all_anagrams(original: str, check: str) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []

    for i in range(0, len(original) - len(check) + 1):
        if is_anagram(original[i: i + len(check)], check):
            res.append(i)
    return res

if __name__ == '__main__':
    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(' '.join(map(str, res)))
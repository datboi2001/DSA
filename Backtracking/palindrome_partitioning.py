from typing import List

def partition(s: str) -> List[List[str]]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    part = []

    def isPali(s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


    def dfs(i):
        if i >= len(s):
            res.append(list(part))
            return
        for j in range(i, len(s)):
            if isPali(s, i, j):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()
    dfs(0)
    return res


if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))

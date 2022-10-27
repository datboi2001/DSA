from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []

    def dfs(i: int, cur: List[int], total: int):
        if total == target:
            res.append(list(cur))
            return
        if i >= len(candidates) or total > target:
            return
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


if __name__ == '__main__':
    candidates = [int(x) for x in input().split()]
    target = int(input())
    res = combination_sum(candidates, target)
    for row in res:
        print(' '.join(map(str, row)))

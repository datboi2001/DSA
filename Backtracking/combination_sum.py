from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    :param candidates: list of candidates
    :param target: target sum
    :return: list of all unique combinations of candidates where the candidate
    numbers sum to target
    """
    # WRITE YOUR BRILLIANT CODE HERE
    # Main idea: DFS. For each candidate, we can either include it or not
    # include it. If we include it, we add it to the current list and
    # recursively call the function with the same index. If we don't include
    # it, we call the function with the next index. We stop when the sum of
    # the current list is equal to the target or when the sum is greater than
    # the target or when we reach the end of the list

    # Time complexity: O(2^n) where n is the length of the list
    # Space complexity: O(n) where n is the length of the list
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

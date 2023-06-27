from typing import List
from collections import deque


def num_steps(target: str, deadends: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if "0000" in deadends:
        return -1

    def get_children(lock: str):
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            yield lock[:i] + digit + lock[i + 1:]
            digit = str((int(lock[i]) - 1 + 10) % 10)
            yield lock[:i] + digit + lock[i + 1:]

    queue = deque()
    queue.append(["0000", 0])  # [lock, turns]
    visited = set(deadends)
    while len(queue) > 0:
        lock, turns = queue.popleft()
        if lock == target:
            return turns
        for child in get_children(lock):
            if child not in visited:
                visited.add(child)
                queue.append([child, turns + 1])
    return -1


if __name__ == '__main__':
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)

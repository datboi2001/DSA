from typing import List
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

target = ((1, 2, 3), (4, 5, 0))


def num_steps(init_pos: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0
    moves_map = {init_pos: 0}
    moves_queue = deque([init_pos])
    while len(moves_queue) > 0:
        cur_puzzle = moves_queue.popleft()
        zero_row, zero_col = 0, 0
        for i in range(len(cur_puzzle)):
            for j in range(len(cur_puzzle[0])):
                if cur_puzzle[i][j] == 0:
                    zero_row, zero_col = i, j
                    break
        for delta_row, delta_col in directions:
            new_row, new_col = zero_row + delta_row, zero_col + delta_col
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_state = list(list(line) for line in cur_puzzle)
                new_state[new_row][new_col], new_state[zero_row][zero_col] = new_state[zero_row][zero_col], \
                                                                             new_state[new_row][new_col]
                new_tuple = tuple(tuple(line) for line in new_state)
                if new_tuple not in moves_map:
                    moves_map[new_tuple] = moves_map[cur_puzzle] + 1
                    moves_queue.append(new_tuple)
                    if new_tuple == target:
                        return moves_map[new_tuple]
    return -1


if __name__ == '__main__':
    init_pos = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = num_steps(init_pos)
    print(res)

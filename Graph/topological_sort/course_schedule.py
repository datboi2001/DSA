from typing import List
from collections import defaultdict
from enum import Enum

class State(Enum):
    TO_VISIT = 0
    VISITING = 1
    VISITED = 2

def is_valid_course_schedule(n: int, prerequisites: List[List[int]]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE


    def dfs(start, states):
        states[start] = State.VISITING

        for prereq in graph[start]:
            if states[prereq] == State.VISITED:
                continue

            if states[prereq] == State.VISITING:
                return False
            if not dfs(prereq, states):
                return False

        states[start] = State.VISITED
        return True

    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    states = [State.TO_VISIT for _ in range(n)]

    for i in range(n):
        if not dfs(i, states):
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    prerequisites = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = is_valid_course_schedule(n, prerequisites)
    print('true' if res else 'false')

from typing import List
from collections import defaultdict, deque

def count_prereq(requirements: List[List[str]]):
    prerequisites = defaultdict(list)
    for prereq, task in requirements:
        prerequisites[task].append(prereq)
    return prerequisites


def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    queue = deque()
    prerequisites = count_prereq(requirements)
    for task in tasks:
        if task not in prerequisites:
            queue.append(task)
    while len(queue) > 0:
        cur_task = queue.popleft()
        res.append(cur_task)
        for prereq, task in requirements:
            if cur_task == prereq:
                prerequisites[task].remove(cur_task)
                if len(prerequisites[task]) == 0:
                    queue.append(task)
                break
    return res



if __name__ == '__main__':
    tasks = input().split()
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling(tasks, requirements)
    print(res)